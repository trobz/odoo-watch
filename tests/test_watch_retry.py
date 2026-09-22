"""fetch_with_retry must retry transient failures, not only bad statuses."""

import sys
import time
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import watch


@pytest.fixture(autouse=True)
def _no_sleep(monkeypatch):
    monkeypatch.setattr(time, "sleep", lambda _: None)


def _fake_curl(monkeypatch, sequence):
    calls = []

    def curl_get(url, timeout=60):
        calls.append(url)
        item = sequence.pop(0)
        if isinstance(item, Exception):
            raise item
        return item

    monkeypatch.setattr(watch, "curl_get", curl_get)
    return calls


def test_retries_transport_failure_then_succeeds(monkeypatch):
    calls = _fake_curl(monkeypatch, [watch.FetchError("http://x", "curl exit 28"), (200, b"<html/>")])
    assert watch.fetch_with_retry("http://x") == b"<html/>"
    assert len(calls) == 2


def test_retries_transient_status_then_succeeds(monkeypatch):
    calls = _fake_curl(monkeypatch, [(403, b""), (429, b""), (200, b"ok")])
    assert watch.fetch_with_retry("http://x") == b"ok"
    assert len(calls) == 3


def test_raises_after_last_attempt(monkeypatch):
    calls = _fake_curl(monkeypatch, [watch.FetchError("http://x", "curl exit 28")] * 3)
    with pytest.raises(watch.FetchError):
        watch.fetch_with_retry("http://x")
    assert len(calls) == 3


def test_does_not_retry_permanent_status(monkeypatch):
    calls = _fake_curl(monkeypatch, [(404, b"")])
    with pytest.raises(watch.FetchError):
        watch.fetch_with_retry("http://x")
    assert len(calls) == 1


def test_with_page_sets_query_param():
    # f"{url}/page/2" would produce "...?country_id=232/page/2" -> 0 results
    assert (
        watch.with_page("https://www.odoo.com/partners?country_id=232", 2)
        == "https://www.odoo.com/partners?country_id=232&page=2"
    )
    assert watch.with_page("https://x/p?page=2", 3) == "https://x/p?page=3"
