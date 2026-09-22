import json
import re
import unicodedata

from bs4 import NavigableString, Tag

SLUG_STRIP_RE = re.compile(r"[^a-z0-9]+")

STRONG_TAGS = ("strong", "b")
EMPHASIS_TAGS = ("em", "i")
TRANSPARENT_TAGS = ("span", "font", "u", "small", "sup", "sub")
INLINE_TAGS = STRONG_TAGS + EMPHASIS_TAGS + TRANSPARENT_TAGS + ("a", "br", "code")

WS_RE = re.compile(r"\s+")
BOLD_STYLE_RE = re.compile(r"font-weight:\s*(bold|700)", re.IGNORECASE)


def fold_version(major: int, minor: int) -> str:
    """Alpha minors belong to the next published major: 18.4 -> 19.0."""
    return f"{major + 1}.0" if minor > 0 else f"{major}.0"


def slugify(text: str) -> str:
    """ASCII, lowercase, dash-separated slug of an app-section title."""
    ascii_text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("ascii")
    return SLUG_STRIP_RE.sub("-", ascii_text.lower()).strip("-")


def stable_id(version: str, app_slug: str, title: str) -> str:
    """`<version>-<app-slug>-<identity-slug>`; identity derives from the item's
    heading text only, so reorder and body wording changes never move it.
    """
    identity_slug = slugify(title)
    if not identity_slug:
        raise ValueError(
            f"{version}/{app_slug}: item title {title!r} yields an empty identity slug"
        )
    return f"{version}-{app_slug}-{identity_slug}"


def normalize_version(version: str) -> str:
    """`"16"` -> `"16.0"`; an already-qualified version is returned unchanged."""
    version = version.strip()
    return version if "." in version else f"{version}.0"


def text(node) -> str:
    return WS_RE.sub(" ", node.get_text()).strip()


def inline(node, where: str) -> str:
    if isinstance(node, NavigableString):
        return WS_RE.sub(" ", str(node))
    if node.name in STRONG_TAGS:
        inner = inline_children(node, where).strip()
        return f"**{inner}**" if inner else ""
    if node.name in EMPHASIS_TAGS:
        inner = inline_children(node, where).strip()
        return f"_{inner}_" if inner else ""
    if node.name == "a":
        inner = inline_children(node, where).strip()
        href = node.get("href", "").strip()
        return f"[{inner}]({href})" if href else inner
    if node.name == "code":
        inner = inline_children(node, where).strip()
        return f"`{inner}`" if inner else ""
    if node.name in TRANSPARENT_TAGS:
        return inline_children(node, where)
    if node.name == "br":
        return "  \n"
    if node.name == "p" and not node.get_text(strip=True) and not element_children(node):
        # Draft-page artifact: an empty <p></p> left inside inline markup
        # (observed inside a <span> in an alpha release-notes page) carries no
        # content and is dropped rather than treated as a structural error.
        return ""
    raise ValueError(f"{where}: unexpected inline tag <{node.name}>")


def inline_children(node: Tag, where: str) -> str:
    return "".join(inline(c, where) for c in node.children)


def paragraph(node: Tag, where: str) -> str:
    lines = [l.strip() for l in inline_children(node, where).split("\n")]
    return "\n".join(l for l in lines if l)


def list_item(li: Tag, where: str) -> list[str]:
    """Lines for one list item: text first, nested blocks as indented lines."""
    lines: list[str] = []
    buffer: list[str] = []

    def flush() -> None:
        text_ = WS_RE.sub(" ", "".join(buffer)).strip()
        buffer.clear()
        if text_:
            lines.append(text_)

    for child in li.children:
        if isinstance(child, NavigableString) or (
            isinstance(child, Tag)
            and child.name in INLINE_TAGS
            and not is_video(child)
        ):
            buffer.append(inline(child, where))
        elif child.name in ("p", "div"):
            flush()
            rendered = paragraph(child, where)
            if rendered:
                lines.append(rendered.replace("\n", " "))
        elif child.name in ("ul", "ol"):
            flush()
            for block in list_block(child, where):
                lines.extend(block.splitlines())
        else:
            raise ValueError(f"{where}: unexpected <{child.name}> inside <li>")
    flush()
    return lines


def is_video(node) -> bool:
    return isinstance(node, Tag) and node.name == "div" and "media_iframe_video" in (
        node.get("class") or []
    )


def element_children(node: Tag) -> list[Tag]:
    return [c for c in node.children if isinstance(c, Tag)]


def list_block(node: Tag, where: str) -> list[str]:
    """List lines as one block, plus any stray non-`li` paragraph as its own block.

    Marketing markup occasionally closes a `<ul>` with a trailing `<p>`.
    """
    ordered = node.name == "ol"
    lines: list[str] = []
    trailing: list[str] = []
    index = 0
    for child in element_children(node):
        if child.name == "li":
            index += 1
            item_lines = list_item(child, where)
            if not item_lines:
                continue
            marker = f"{index}. " if ordered else "- "
            lines.append(marker + item_lines[0])
            lines.extend("  " + l for l in item_lines[1:])
        elif child.name in ("p", "div"):
            rendered = paragraph(child, where)
            if rendered:
                trailing.append(rendered)
        else:
            raise ValueError(f"{where}: unexpected <{child.name}> inside <{node.name}>")
    blocks = ["\n".join(lines)] if lines else []
    return blocks + trailing


def video_link(node: Tag, where: str) -> str:
    expression = (node.get("data-oe-expression") or "").strip()
    if not expression:
        raise ValueError(f"{where}: media_iframe_video without data-oe-expression")
    url = f"https:{expression}" if expression.startswith("//") else expression
    return f"[Video]({url})"


def block_nodes(nodes, where: str) -> str:
    """Render an explicit list of sibling nodes as markdown blocks.

    `h3`-`h6` are accepted as body blocks (needed for the archived item-body
    quirk in `release_notes.split_column_items`); this also loosens the
    live-path guard, but no 16.0+ item body places a heading, so it is
    currently inert there.
    """
    blocks: list[str] = []
    for child in nodes:
        if isinstance(child, NavigableString):
            text_ = WS_RE.sub(" ", str(child)).strip()
            if text_:
                blocks.append(text_)
            continue
        if is_video(child):
            blocks.append(video_link(child, where))
        elif child.name in ("p", "div", "h3", "h4", "h5", "h6"):
            rendered = paragraph(child, where)
            if rendered:
                blocks.append(rendered)
        elif child.name in ("ul", "ol"):
            blocks.extend(list_block(child, where))
        elif child.name == "br":
            continue
        elif child.name in INLINE_TAGS:
            rendered = inline(child, where).strip()
            if rendered:
                blocks.append(rendered)
        else:
            raise ValueError(f"{where}: unexpected block tag <{child.name}>")
    return "\n\n".join(blocks)


def blocks(item: Tag, title_node, where: str) -> str:
    return block_nodes([c for c in item.children if c is not title_node], where)


def frontmatter(version: str, app: str, app_slug: str, source_url: str, item_count: int) -> str:
    """`FRONTMATTER_KEYS`-compliant `---`-fenced header block, no trailing blank line."""
    lines = [
        "---",
        f"version: {json.dumps(version)}",
        f"app: {json.dumps(app)}",
        f"app_slug: {json.dumps(app_slug)}",
        f"source_url: {json.dumps(source_url)}",
        f"item_count: {item_count}",
        "---",
    ]
    return "\n".join(lines) + "\n"
