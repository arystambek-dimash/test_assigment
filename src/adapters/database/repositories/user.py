from dataclasses import asdict
from typing import Union

from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession

from src.adapters.database.models.user import User
from src.domain.entities.user import UserDTO, UserCrudDTO


class UserRepository:
    def __init__(self, session: AsyncSession):
        self._session = session

    async def add(self, user: UserCrudDTO) -> UserDTO:
        stmt = insert(User).values(**asdict(user)).returning(User)
        result = await self._session.execute(stmt)
        inserted_user = result.scalar_one()
        return self._map_to_dto(inserted_user)

    async def get_by_id(self, user_id: int) -> Union[UserDTO, None]:
        stmt = select(User).where(User.id == user_id)
        result = await self._session.execute(stmt)
        user = result.scalar_one_or_none()
        if user:
            return self._map_to_dto(user)
        return None

    async def get_by_username(self, username: str) -> Union[UserDTO, None]:
        stmt = select(User).where(User.username == username)
        result = await self._session.execute(stmt)
        user = result.scalar_one_or_none()
        if user:
            return self._map_to_dto(user)
        return None

    @staticmethod
    def _map_to_dto(entity: User) -> UserDTO:
        return UserDTO(
            id=entity.id,
            username=entity.username,
            password=entity.password
        )
