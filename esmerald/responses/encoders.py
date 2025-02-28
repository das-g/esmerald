from typing import Any

from starlette.responses import JSONResponse as JSONResponse

from esmerald.responses.json import BaseJSONResponse

try:
    import orjson
    from orjson import OPT_OMIT_MICROSECONDS, OPT_SERIALIZE_NUMPY
except ImportError:  # pragma: no cover
    orjson = None

try:
    import ujson
except ImportError:  # pragma: no cover
    ujson = None


class ORJSONResponse(BaseJSONResponse):
    def render(self, content: Any) -> bytes:
        assert orjson is not None, "You must install the encoders or orjson to use ORJSONResponse"
        return orjson.dumps(
            content,
            default=self.transform,
            option=OPT_SERIALIZE_NUMPY | OPT_OMIT_MICROSECONDS,
        )


class UJSONResponse(BaseJSONResponse):
    def render(self, content: Any) -> bytes:
        assert ujson is not None, "You must install the encoders or ujson to use UJSONResponse"
        return ujson.dumps(content, ensure_ascii=False).encode("utf-8")
