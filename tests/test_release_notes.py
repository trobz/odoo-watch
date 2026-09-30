import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import release_notes


def test_misnested_il_tag_splits_into_two_sibling_li_elements():
    """Upstream authoring typo: `<il>text1<li>text2</li></il>` must become two
    sibling `<li>` elements before parsing."""
    html = "<ul><il>text1<li>text2</li></il></ul>"
    fixed = release_notes.MISNESTED_IL_RE.sub(r"<li>\1</li><li>\2</li>", html)
    assert fixed == "<ul><li>text1</li><li>text2</li></ul>"
