
from netease.crypto import eapi


def test_eapi_returns_params():
    result = eapi(
        "/api/test",
        {
            "hello": "world"
        }
    )

    assert result.startswith("params=")
    assert len(result) > len("params=")
