from io import StringIO

try:
    from js import XMLHttpRequest  # type: ignore[import-not-found]
except ImportError:
    pass


class Response:  # pylint: disable=too-few-public-methods
    def __init__(self, fetch_response: object) -> None:
        self.status_code = int(fetch_response.status)  # type: ignore[attr-defined]
        self.text = str(StringIO(fetch_response.response))  # type: ignore[attr-defined]


def get(url: str) -> Response:
    """
    HTTP GET url and return an object with two properties,
    status_code and text.
    """
    req = XMLHttpRequest.new()
    req.open("GET", url, False)
    req.send(None)
    return Response(req)
