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


def test_check_expected_rejects_other_country():
    # odoo.com falls back to geo-IP defaults for some URL forms; a US listing
    # must not be saved as the Vietnam one.
    watch.check_expected("A [Gold] /partners/a-1?country_id=232\n", "country_id=232")
    with pytest.raises(ValueError, match="country_id=232"):
        watch.check_expected("B [Ready] /partners/b-2?country_id=224\n", "country_id=232")
