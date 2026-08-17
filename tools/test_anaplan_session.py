import pytest
import requests

from anaplan_session import (
    AnaplanAuthError,
    AnaplanError,
    AnaplanSession,
    AnaplanTimeoutError,
    AnaplanTooLargeError,
    AnaplanURLNotAllowedError,
    classify_response,
    is_url_allowed,
)

BASE = "https://api.anaplan.com"
MID = "84FF020411B04FD9818004D84C9A5DCE"


def test_allows_view_data_with_required_format():
    assert is_url_allowed(f"{BASE}/2/0/models/{MID}/views/102000000025/data?format=v1")


def test_allows_view_data_with_pages_param():
    assert is_url_allowed(
        f"{BASE}/2/0/models/{MID}/views/102000000025/data"
        f"?format=v1&pages=101000000007:214000000002")


def test_allows_metadata_endpoints():
    assert is_url_allowed(f"{BASE}/2/0/models/{MID}/views")
    assert is_url_allowed(f"{BASE}/2/0/models/{MID}/views/102000000025")
    assert is_url_allowed(f"{BASE}/2/0/models/{MID}/lists")
    assert is_url_allowed(f"{BASE}/2/0/models/{MID}/lists/101000000012/items")


def test_rejects_app_shard_host():
    """The regional app shard redirects /2/0/ to the global endpoint, which
    rejects web-session cookies with 401. Calling it is always a mistake."""
    assert not is_url_allowed(
        f"https://eu2a.app.anaplan.com/2/0/models/{MID}/views/1/data?format=v1")


def test_rejects_write_shaped_and_unrelated_urls():
    assert not is_url_allowed(f"{BASE}/2/0/models/{MID}/imports/1/tasks")
    assert not is_url_allowed(f"{BASE}/2/0/models/{MID}/exports/1/tasks")
    assert not is_url_allowed("https://evil.example.com/2/0/models/X/views/1/data")
    assert not is_url_allowed(f"{BASE}/2/0/workspaces/{MID}/models")


def test_classify_ok_returns_none():
    assert classify_response(200, "application/json", '{"rows":[]}') is None


def test_classify_401_raises_auth():
    with pytest.raises(AnaplanAuthError):
        classify_response(401, "application/json",
                          '{"status":{"code":401,"message":"Not Authenticated."}}')


def test_classify_403_raises_auth():
    with pytest.raises(AnaplanAuthError):
        classify_response(403, "application/json", '{"status":"forbidden"}')


def test_classify_400_too_large_raises_too_large():
    with pytest.raises(AnaplanTooLargeError):
        classify_response(400, "application/json",
                          '{"status":{"message":"The view is too large to export"}}')


def test_classify_400_missing_format_is_generic_not_too_large():
    """Verbatim body observed 2026-08-14. Misreading this as 'too large' would
    tell the agent to narrow when the real fix is to send format=v1."""
    with pytest.raises(AnaplanError) as exc:
        classify_response(400, "application/json",
                          '{"status":{"code":400,"message":"Mandatory query '
                          'parameter \'format\' is missing"}}')
    assert not isinstance(exc.value, AnaplanTooLargeError)


def test_classify_400_malformed_pages_is_generic_not_too_large():
    """Also observed verbatim. Same trap."""
    with pytest.raises(AnaplanError) as exc:
        classify_response(400, "application/json",
                          '{"status":{"code":400,"message":"Malformed pages '
                          'parameter [214000000002]"}}')
    assert not isinstance(exc.value, AnaplanTooLargeError)


def test_classify_200_non_json_content_type_raises():
    with pytest.raises(AnaplanError):
        classify_response(200, "text/html", "<html>session expired</html>")


def test_classify_200_undecodable_body_raises():
    """OBSERVED 2026-08-14: a view returned HTTP 200 with a body json() could
    not decode. A Content-Type check alone lets this through and the caller
    then gets a raw JSONDecodeError, escaping the typed-error contract."""
    with pytest.raises(AnaplanError):
        classify_response(200, "application/json", "")


def test_too_large_error_carries_page_dimensions():
    err = AnaplanTooLargeError("too big", page_dimensions=["Product", "Region"])
    assert err.page_dimensions == ["Product", "Region"]


class FakeResponse:
    def __init__(self, status_code=200, content_type="application/json", text='{"ok":1}'):
        self.status_code = status_code
        self.headers = {"Content-Type": content_type}
        self.text = text

    def json(self):
        import json as _json
        return _json.loads(self.text)


class FakeRequests:
    """Minimal stand-in for requests.Session. Only HTTP status codes are
    simulated - no assumptions about Anaplan payload shapes."""

    def __init__(self, responses):
        self._responses = list(responses)
        self.calls = []

    def get(self, url, timeout=None):
        self.calls.append(url)
        item = self._responses.pop(0)
        if isinstance(item, Exception):
            raise item
        return item

    def close(self):
        pass


def test_get_rejects_disallowed_url():
    sess = AnaplanSession(BASE, FakeRequests([]))
    with pytest.raises(AnaplanURLNotAllowedError):
        sess.get(f"{BASE}/2/0/models/{MID}/exports/1/tasks")


def test_get_returns_parsed_json():
    fake = FakeRequests([FakeResponse(text='{"views":[]}')])
    sess = AnaplanSession(BASE, fake)
    assert sess.get(f"{BASE}/2/0/models/{MID}/views") == {"views": []}


def test_get_maps_timeout_to_typed_error():
    fake = FakeRequests([requests.Timeout("timed out")])
    sess = AnaplanSession(BASE, fake)
    with pytest.raises(AnaplanTimeoutError):
        sess.get(f"{BASE}/2/0/models/{MID}/views")


def test_get_raises_typed_error_on_undecodable_200():
    """The observed 200-with-bad-body must surface as AnaplanError, never as a
    bare JSONDecodeError escaping to the CLI."""
    fake = FakeRequests([FakeResponse(text="")])
    sess = AnaplanSession(BASE, fake)
    with pytest.raises(AnaplanError):
        sess.get(f"{BASE}/2/0/models/{MID}/views")


def test_get_refreshes_token_once_then_succeeds():
    """A 401 mid-run means the ~30 min token expired. One refresh, then retry."""
    fake = FakeRequests([FakeResponse(status_code=401, text='{"m":"no"}'),
                         FakeResponse(text='{"views":[]}')])
    sess = AnaplanSession(BASE, fake)
    calls = []
    sess._refresh = lambda: calls.append("refresh")
    assert sess.get(f"{BASE}/2/0/models/{MID}/views") == {"views": []}
    assert calls == ["refresh"]


def test_get_gives_up_after_second_auth_failure():
    fake = FakeRequests([FakeResponse(status_code=401, text='{"m":"no"}'),
                         FakeResponse(status_code=401, text='{"m":"no again"}')])
    sess = AnaplanSession(BASE, fake)
    sess._refresh = lambda: None
    with pytest.raises(AnaplanAuthError):
        sess.get(f"{BASE}/2/0/models/{MID}/views")


def test_session_has_no_write_methods():
    """Structural read-only guarantee from the design. If this fails, someone
    added a write path - that must be a deliberate, reviewed decision."""
    for verb in ("post", "put", "patch", "delete"):
        assert not hasattr(AnaplanSession, verb)
