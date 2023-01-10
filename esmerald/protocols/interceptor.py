from typing import TYPE_CHECKING, TypeVar

from typing_extensions import Protocol, runtime_checkable

from esmerald.requests import Request

if TYPE_CHECKING:
    from starlette.types import ASGIApp, Receive, Scope, Send

T = TypeVar("T")


@runtime_checkable
class InterceptorProtocol(Protocol):  # pragma: no cover
    """
    Generic object serving the base for interception of messages,
    before reaching the endpoint. This is inspired by the AOP (Aspect Oriented Programming).

    The interceptor is handled between the call and the API endpoint itself and acts on it.

    An interceptor could be anything from logging to rerouting or even input sanitizing.
    """

    def __init__(self, app: "ASGIApp") -> None:
        ...

    async def __call__(self, scope: "Scope", send: "Send", receive: "Receive") -> None:
        ...
