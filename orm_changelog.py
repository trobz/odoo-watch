import json
import re

from bs4 import BeautifulSoup, Tag

from utils import fold_version, frontmatter, list_item, stable_id


class OrmChangelogError(ValueError):
    """Raised when the ORM changelog page markup does not match the expected
    structure, or when an item cannot be rendered unambiguously.
    """


VERSION_HEADING_RE = re.compile(r"^Odoo (?:Online )?version (\d+)\.(\d+)$")
CHROME_VERSION_RE = re.compile(r"^Odoo .*version", re.IGNORECASE)
SENTENCE_BREAK_RE = re.compile(r"\.(?=\s|$)")

APP_NAME = "ORM API"
APP_SLUG = "orm-api"


def heading_text(h2: Tag) -> str:
    """Flattened heading text with the trailing `¶` headerlink stripped."""
    raw = re.sub(r"\s+", " ", h2.get_text()).strip()
    return raw.rstrip("\u00b6").strip()


def flatten_item(li: Tag, where: str) -> str:
    try:
        lines = list_item(li, where)
    except ValueError as e:
        raise OrmChangelogError(str(e)) from e
    return " ".join(l.strip() for l in lines if l.strip())


def split_title_body(text: str, where: str) -> tuple[str, str]:
    """Split at the first sentence break; a title without one is the full item text.

    No length cap: the analyzer's release-notes UI clamps long titles to two lines
    with a hover tooltip for the full text, so truncating here would only destroy
    information (a single-sentence title has no body to move the tail into).
    """
    match = SENTENCE_BREAK_RE.search(text)
    if match:
        title = text[: match.start()].strip()
        body = text[match.end() :].strip()
    else:
        title = text.strip()
        body = ""

    if not title:
        raise OrmChangelogError(f"{where}: item text {text!r} yields an empty title")
    return title, body


def render_markdown(major: str, items: list, source_url: str) -> str:
    fm = frontmatter(major, APP_NAME, APP_SLUG, source_url, len(items))
    heading = f"# {APP_NAME} changelog ({major})"
    parts = [f"## {title}\n\n{body}".rstrip() for title, _doc_version, body in items]
    return fm + "\n" + heading + "\n\n" + "\n\n".join(parts) + "\n"


def parse(html: str, source_url: str) -> dict[str, str]:
    """Parse the ORM changelog page into `{"{major}.0/orm-api.md": markdown,
    "{major}.0/index.json": json, ...}`, one pair per major version found.

    Raises `OrmChangelogError` on markup that does not match the expected
    structure (see plan failure policy). Never network I/O.
    """
    soup = BeautifulSoup(html, "html.parser")

    majors: dict[str, list] = {}
    current_major: str | None = None
    current_doc_version: str | None = None
    current_items: list | None = None

    def close_current() -> None:
        if current_major is not None and not current_items:
            raise OrmChangelogError(
                f"{current_doc_version!r}: version heading yielded 0 items"
            )

    for node in soup.find_all(["h2", "li"]):
        if node.name == "h2":
            close_current()
            text = heading_text(node)
            match = VERSION_HEADING_RE.match(text)
            if match:
                major, minor = match.groups()
                # Alpha/beta minors belong to the next published major (user rule 2026-09-21).
                current_major = fold_version(int(major), int(minor))
                current_doc_version = text
                current_items = majors.setdefault(current_major, [])
            elif CHROME_VERSION_RE.match(text):
                raise OrmChangelogError(
                    f"unrecognized version heading (does not match the folding "
                    f"pattern): {text!r}"
                )
            else:
                current_major = None
                current_doc_version = None
                current_items = None
            continue

        # li
        parent = node.parent
        if not (
            isinstance(parent, Tag)
            and parent.name == "ul"
            and "simple" in (parent.get("class") or [])
        ):
            continue  # not a content list item (e.g. sidebar/nav chrome)
        if current_major is None:
            raise OrmChangelogError("item <li> found outside any version heading")

        where = f"{current_major} / {current_doc_version}"
        flattened = flatten_item(node, where)
        title, body = split_title_body(flattened, where)
        current_items.append((title, current_doc_version, body))

    close_current()

    if not majors:
        raise OrmChangelogError("no version headings found on the ORM changelog page")

    outputs: dict[str, str] = {}
    for major, items in majors.items():
        outputs[f"{major}/orm-api.md"] = render_markdown(major, items, source_url)

        notes = []
        seen_ids: dict[str, int] = {}
        for title, _doc_version, _body in items:
            where = f"{major} / {title}"
            try:
                base_id = stable_id(major, APP_SLUG, title)
            except ValueError as e:
                raise OrmChangelogError(str(e)) from e
            count = seen_ids.get(base_id, 0) + 1
            seen_ids[base_id] = count
            note_id = base_id if count == 1 else f"{base_id}-{count}"
            notes.append({"id": note_id, "title": title})

        index = {
            "version": major,
            "source_url": source_url,
            "apps": [
                {
                    "app": APP_NAME,
                    "slug": APP_SLUG,
                    "file": "orm-api.md",
                    "anchor": "",
                    "item_count": len(items),
                    "notes": notes,
                }
            ],
            "item_count": len(items),
        }
        outputs[f"{major}/index.json"] = (
            json.dumps(index, sort_keys=False, indent=2, ensure_ascii=False) + "\n"
        )

    return outputs
