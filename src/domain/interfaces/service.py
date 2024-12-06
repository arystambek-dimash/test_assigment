from typing import Protocol, TypeVar, Dict

T = TypeVar('T', bound=str)
V = TypeVar('V', bound=Dict[str, str])


class JWTService(Protocol):
    def decode(self, token: T, token_type: str) -> V:
        ...

    def encode(self, payload: V, token_type: str) -> T:
        ...
