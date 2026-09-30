import json
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import orm_changelog

FIXTURES = Path(__file__).resolve().parent / "fixtures"


def _fixture_html(name: str) -> str:
    return (FIXTURES / name).read_text(encoding="utf-8")


def test_parse_item_counts_match_fixture():
    html = _fixture_html("orm_changelog_sample.html")
    outputs = orm_changelog.parse(html, "https://example.test/orm-changelog")

    index_18 = json.loads(outputs["18.0/index.json"])
    assert index_18["item_count"] == 4
    assert len(index_18["apps"][0]["notes"]) == 4

    index_19 = json.loads(outputs["19.0/index.json"])
    assert index_19["item_count"] == 2
    assert len(index_19["apps"][0]["notes"]) == 2


def test_alpha_minor_folds_into_next_major():
    """Odoo version 18.4 (an alpha minor) folds into the 19.0 major, not 18.4."""
    html = _fixture_html("orm_changelog_sample.html")
    outputs = orm_changelog.parse(html, "https://example.test/orm-changelog")
    assert "19.0/orm-api.md" in outputs
    assert "18.4/orm-api.md" not in outputs
    md = outputs["19.0/orm-api.md"]
    assert "Alpha-fold item merges into next major" in md
    assert "Second alpha-fold item" in md


def test_duplicate_title_gets_suffixed_id():
    html = _fixture_html("orm_changelog_sample.html")
    outputs = orm_changelog.parse(html, "https://example.test/orm-changelog")
    notes = json.loads(outputs["18.0/index.json"])["apps"][0]["notes"]
    ids = [n["id"] for n in notes]
    dup_ids = [
        i for i in ids if i.startswith("18.0-orm-api-add-support-for-new-field-types")
    ]
    assert dup_ids == [
        "18.0-orm-api-add-support-for-new-field-types",
        "18.0-orm-api-add-support-for-new-field-types-2",
    ]


def test_split_title_body_preserves_version_number():
    """A period between two digits with a stray space inserted around the
    decimal point ('3. 11') is not a sentence break."""
    text = "Requires Python 3. 11 or later"
    title, body = orm_changelog.split_title_body(text, "where")
    assert title == text
    assert body == ""


def test_split_title_body_preserves_abbreviation():
    """A period followed by whitespace and a lowercase word ('e.g. foo') is not
    a sentence break."""
    text = "Improve handling, e.g. foo bar edge cases"
    title, body = orm_changelog.split_title_body(text, "where")
    assert title == text
    assert body == ""


def test_split_title_body_still_splits_on_real_sentence_break():
    text = "Add support for new field types. See the migration guide for details."
    title, body = orm_changelog.split_title_body(text, "where")
    assert title == "Add support for new field types"
    assert body == "See the migration guide for details."


def test_split_title_body_empty_title_raises():
    with pytest.raises(orm_changelog.OrmChangelogError):
        orm_changelog.split_title_body(". Some body.", "where")
