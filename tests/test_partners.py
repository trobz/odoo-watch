import sys
import types

sys.modules.setdefault("openai", types.SimpleNamespace(OpenAI=None))

import describe_changes
from watch import sort_partners


def test_sort_partners_orders_by_tier_then_name():
    content = "b [Ready] /b\nA [Silver] /a\nc [Gold] /c\n"
    assert sort_partners(content) == "c [Gold] /c\nA [Silver] /a\nb [Ready] /b\n"


def test_sort_partners_ignores_input_order():
    one = "a [Ready] /a\nb [Ready] /b\n"
    two = "b [Ready] /b\na [Ready] /a\n"
    assert sort_partners(one) == sort_partners(two)


def test_describe_partners_ignores_reorder_reports_changes(monkeypatch):
    old = "a [Ready] /a\nb [Silver] /b\nc [Ready] /c\n"
    new = "c [Ready] /c\nb [Gold] /b\nd [Ready] /d\n"
    outputs = {"HEAD~1": old, "HEAD": new}
    monkeypatch.setattr(
        describe_changes, "git", lambda *a, check=True: outputs[a[1].split(":")[0]]
    )
    result = describe_changes.describe_partners()
    assert "- Added: d [Ready]" in result
    assert "- Removed: a [Ready]" in result
    assert "- Tier change: b [Silver] -> [Gold]" in result
    assert "c [" not in result
