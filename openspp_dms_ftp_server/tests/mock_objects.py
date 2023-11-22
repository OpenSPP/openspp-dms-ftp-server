import json
from typing import Any

from requests import Response


class MockResponse(Response):
    def __init__(
        self,
        url="http://example.com",
        headers=None,
        status_code=200,
        reason="Success",
        _content="",
        json_=None,
        encoding="UTF-8",
    ):
        if headers is None:
            headers = {"Content-Type": "text/html; charset=UTF-8"}
        self.url = url
        self.headers = headers
        if json_ and headers["Content-Type"] == "application/json":
            self._content = json.dumps(json_).encode(encoding)
        else:
            self._content = _content.encode(encoding)
        self.status_code = status_code
        self.reason = reason
        self.encoding = encoding

    def json(self, *args, **kwargs) -> Any:
        if not self._content:
            return {}
        return json.loads(self._content)
