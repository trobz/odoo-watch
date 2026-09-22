import json
import re

from bs4 import BeautifulSoup, Tag

from utils import (
    block_nodes,
    blocks,
    element_children,
    inline_children,
    slugify,
    stable_id,
    text,
    normalize_version,
    STRONG_TAGS,
)

SECTION_ANCHOR_PREFIX = "table_of_content_heading"
ITEM_CLASS = "col-lg-6"

HEADING_TITLE_TAGS = ("h3", "h4", "h5", "h6")

WS_RE = re.compile(r"\s+")
BOLD_STYLE_RE = re.compile(r"font-weight:\s*(bold|700)", re.IGNORECASE)
NON_BOLD_STYLE_RE = re.compile(r"font-weight:\s*([1-4]00|normal)", re.IGNORECASE)


class ReleaseNotesError(ValueError):
    """Raised when the page markup does not match the expected structure."""


ARCHIVED_PINS = {
    "12.0": "20241213201014",
    "13.0": "20260410095156",
    "14.0": "20250615185727",
    "15.0": "20250810140306",
}
ARCHIVED_SNAPSHOT_URL = (
    "http://web.archive.org/web/{ts}id_/https://www.odoo.com/odoo-{major}-release-notes"
)


def is_item(node: Tag) -> bool:
    return node.name == "div" and ITEM_CLASS in (node.get("class") or [])


def is_title_node(node: Tag) -> bool:
    if node.name in HEADING_TITLE_TAGS or node.name in STRONG_TAGS:
        return True
    if node.name != "p":
        return False
    style = (node.get("style") or "").replace(" ", "")
    if BOLD_STYLE_RE.search(style):
        return True
    children = [c for c in element_children(node) if c.name != "br"]
    if len(children) == 1 and children[0].name in STRONG_TAGS:
        return text(children[0]) == text(node)
    return False


def parse_item(item: Tag, where: str) -> tuple[str, str]:
    children = element_children(item)
    title_node = children[0] if children else None
    if title_node is not None and not is_title_node(title_node):
        raise ReleaseNotesError(
            f"{where}: item first element child is <{title_node.name}>, not a title node"
        )
    try:
        title = ""
        if title_node is not None:
            title = inline_children(title_node, where)
            title = WS_RE.sub(" ", title).strip()
            if title_node.name in STRONG_TAGS:
                title = title.strip("*").strip()
        body = blocks(item, title_node, where)
    except ValueError as e:
        raise ReleaseNotesError(str(e)) from e
    if not title and body:
        raise ReleaseNotesError(f"{where}: item has a body but no title")
    return title, body


def sections(soup: BeautifulSoup, version: str) -> list[dict]:
    """Return `[{title, anchor, items: [(title, body)]}]` in document order."""
    result: list[dict] = []
    current: dict | None = None
    for node in soup.find_all(["h2", "div"]):
        if node.name == "h2":
            anchor = node.get("id") or ""
            if anchor.startswith(SECTION_ANCHOR_PREFIX) and text(node):
                current = {"title": text(node), "anchor": anchor, "items": []}
                result.append(current)
            else:
                current = None  # known chrome: unanchored or empty-text h2
            continue
        if not is_item(node):
            continue
        if current is None:
            raise ReleaseNotesError(
                f"{version}: item div.{ITEM_CLASS} outside any anchored section"
            )
        where = f"{version} / {current['title']}"
        title, body = parse_item(node, where)
        if not title and not body:
            continue  # known placeholder item
        current["items"].append((title, body))
    return result


def is_faux_heading(node: Tag) -> bool:
    """Non-bold-styled heading -- an authoring accident where body text was
    marked up with a heading tag. Checked on the node and its descendants,
    mirroring (inverted) `is_title_node`'s `BOLD_STYLE_RE` heuristic.
    """
    style = (node.get("style") or "").replace(" ", "")
    if NON_BOLD_STYLE_RE.search(style):
        return True
    for descendant in node.find_all(True):
        style = (descendant.get("style") or "").replace(" ", "")
        if NON_BOLD_STYLE_RE.search(style):
            return True
    return False


def split_column_items(col: Tag, where: str) -> list[tuple[str, str]]:
    """Split one item column into `[(title, body), ...]`.

    A heading (`h3`-`h6`) opens a new item; everything else appends to the
    current item's body. An empty heading is a spacer and is skipped entirely.
    A non-bold ("faux") heading is body text, not a title. Body before any
    heading opens a title-less item so the existing "body but no title" error
    still fires loudly instead of crashing on a missing title.
    """
    raw_items: list[dict] = []
    current: dict | None = None
    for child in col.children:
        if isinstance(child, Tag) and child.name in HEADING_TITLE_TAGS:
            heading_text = text(child)
            if not heading_text:
                continue  # empty heading = spacer, skipped entirely
            if is_faux_heading(child):
                if current is None:
                    current = {"title": "", "body": []}
                    raw_items.append(current)
                current["body"].append(child)
                continue
            title = WS_RE.sub(" ", inline_children(child, where)).strip()
            current = {"title": title, "body": []}
            raw_items.append(current)
            continue
        if current is None:
            current = {"title": "", "body": []}
            raw_items.append(current)
        current["body"].append(child)

    items: list[tuple[str, str]] = []
    for raw in raw_items:
        try:
            body = block_nodes(raw["body"], where)
        except ValueError as e:
            raise ReleaseNotesError(str(e)) from e
        title = raw["title"]
        if not title and body:
            raise ReleaseNotesError(f"{where}: item has a body but no title")
        if not title and not body:
            continue  # empty title and empty body: known placeholder
        items.append((title, body))
    return items


def archived_sections(soup: BeautifulSoup, version: str) -> list[dict]:
    """Pre-v16 markup: an `<h2>` with no `id`, whose parent is `div.col-lg-12`
    and whose next element sibling is `div.row`, marks a section; item columns
    are the direct child `div`s of that `div.row`. See plan Phase 2 for the
    measured cases each rule guards.
    """
    result: list[dict] = []
    for h2 in soup.find_all("h2"):
        parent = h2.parent
        if not (
            isinstance(parent, Tag)
            and parent.name == "div"
            and "col-lg-12" in (parent.get("class") or [])
        ):
            continue
        sib = h2.find_next_sibling()
        if not (
            isinstance(sib, Tag)
            and sib.name == "div"
            and "row" in (sib.get("class") or [])
        ):
            continue
        title = text(h2)
        if not title:
            continue
        where = f"{version} / {title}"
        items: list[tuple[str, str]] = []
        for col in element_children(sib):
            items.extend(split_column_items(col, where))
        result.append({"title": title, "anchor": "", "items": items})
    return result


def render_markdown(section: dict, slug: str, version: str, source_url: str) -> str:
    app = section["title"]
    url = f"{source_url}#{section['anchor']}" if section["anchor"] else source_url
    lines = [
        "---",
        f"version: {json.dumps(version)}",
        f"app: {json.dumps(app)}",
        f"app_slug: {json.dumps(slug)}",
        f"source_url: {json.dumps(url)}",
        f"item_count: {len(section['items'])}",
        "---",
        "",
        f"# {app} — Odoo {version}",
    ]
    body_parts = []
    for title, body in section["items"]:
        part = f"## {title}" if title else ""
        if body:
            part = f"{part}\n\n{body}" if part else body
        body_parts.append(part)
    header = "\n".join(lines) + "\n"
    return header + "\n" + "\n\n".join(body_parts) + "\n"


def build_index(apps: list[dict], total: int, version: str, source_url) -> str:
    index = {"version": version}
    if isinstance(source_url, list):
        index["source_urls"] = source_url
    else:
        index["source_url"] = source_url
    index["apps"] = apps
    index["item_count"] = total
    return json.dumps(index, sort_keys=False, indent=2, ensure_ascii=False) + "\n"


def merge_page_sections(per_page: list[tuple[list[dict], str]]) -> list[dict]:
    """Merge same-titled sections from several pages, in first-seen order.

    An alpha-fold target (e.g. 19.1-19.4 folding into 20.0) is announced across
    several incremental pages that each cover the same set of apps; an app's
    items across those pages concatenate in page order. Each merged section
    keeps the url of the page it first appeared on, for its markdown link.
    """
    merged: dict[str, dict] = {}
    order: list[str] = []
    for page_sections, url in per_page:
        for section in page_sections:
            key = section["title"]
            if key not in merged:
                merged[key] = {
                    "title": section["title"],
                    "anchor": section["anchor"],
                    "items": list(section["items"]),
                    "source_url": url,
                }
                order.append(key)
            else:
                merged[key]["items"].extend(section["items"])
    return [merged[key] for key in order]


def _parse_pages(pages: list[tuple[str, str]], version: str) -> dict[str, str]:
    per_page: list[tuple[list[dict], str]] = []
    for html, url in pages:
        soup = BeautifulSoup(html, "html.parser")
        page_sections = (
            archived_sections(soup, version)
            if version in ARCHIVED_PINS
            else sections(soup, version)
        )
        if not page_sections:
            raise ReleaseNotesError(f"{version}: no app sections found ({url})")
        per_page.append((page_sections, url))

    if len(pages) == 1:
        page_sections = per_page[0][0]
        page_url = per_page[0][1]
        section_url = lambda _section: page_url  # noqa: E731
        index_source_url = page_url
    else:
        page_sections = merge_page_sections(per_page)
        section_url = lambda section: section["source_url"]  # noqa: E731
        index_source_url = [url for _html, url in pages]

    outputs: dict[str, str] = {}
    apps = []
    seen_slugs: dict[str, str] = {}
    seen_ids: dict[str, int] = {}
    total = 0
    for section in page_sections:
        if not section["items"]:
            raise ReleaseNotesError(
                f"{version}: section {section['title']!r} yielded 0 items"
            )
        slug = slugify(section["title"])
        if not slug:
            raise ReleaseNotesError(
                f"{version}: section {section['title']!r} has an empty slug"
            )
        if slug in seen_slugs:
            raise ReleaseNotesError(
                f"{version}: duplicate slug {slug!r} from {section['title']!r} "
                f"and {seen_slugs[slug]!r}"
            )
        seen_slugs[slug] = section["title"]
        filename = f"{slug}.md"
        outputs[f"{version}/{filename}"] = render_markdown(
            section, slug, version, section_url(section)
        )
        notes = []
        for title, _body in section["items"]:
            try:
                base_id = stable_id(version, slug, title)
            except ValueError as e:
                raise ReleaseNotesError(str(e)) from e
            # Odoo occasionally repeats a heading verbatim for two distinct
            # features in one app; disambiguate deterministically instead of
            # failing the whole corpus. Items are otherwise indistinguishable
            # by title, so only their mutual order affects which gets the
            # suffix -- everything else about identity stays reorder-stable.
            count = seen_ids.get(base_id, 0) + 1
            seen_ids[base_id] = count
            note_id = base_id if count == 1 else f"{base_id}-{count}"
            notes.append({"id": note_id, "title": title})
        apps.append(
            {
                "app": section["title"],
                "slug": slug,
                "file": filename,
                "anchor": section["anchor"],
                "item_count": len(section["items"]),
                "notes": notes,
            }
        )
        total += len(section["items"])

    outputs[f"{version}/index.json"] = build_index(apps, total, version, index_source_url)
    return outputs


def parse(html: str, version: str, source_url: str) -> dict[str, str]:
    return _parse_pages([(html, source_url)], version)


def parse_multi(pages: list[tuple[str, str]], version: str) -> dict[str, str]:
    """Merge 2+ alpha pages that fold into one unpublished major version."""
    if len(pages) < 2:
        raise ValueError("parse_multi requires 2 or more pages")
    return _parse_pages(pages, version)
