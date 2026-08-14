import pytest

from anaplan_session import (
    AnaplanAuthError,
    AnaplanError,
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
