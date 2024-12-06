from typing import Protocol, TypeVar

from src.domain.entities.user import UserDTO, UserCrudDTO

T = TypeVar('T')
V = TypeVar('V')


class Repository(Protocol[T, V]):
    async def add(self, obj: T) -> V:
        ...

    async def get_by_id(self, id: int) -> V:
        ...


class UserRepository(Repository[UserCrudDTO, UserDTO], Protocol):
    async def get_by_username(self, username: str) -> UserDTO:
        ...
