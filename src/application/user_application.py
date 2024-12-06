from src.domain.entities.jwt import Token
from src.domain.entities.user import UserCreateDTO, UserSignDTO
from src.domain.exceptions.base import NotFound, BadRequest
from src.domain.interfaces.repository import UserRepository
from src.domain.interfaces.service import JWTService
from src.domain.interfaces.uow import UoW
from src.domain.value_objects.user import UserPassword


class UserApplication:
    def __init__(self,
                 uow: UoW,
                 user_repository: UserRepository,
                 jwt: JWTService
                 ):
        self._uow = uow
        self._user_repository = user_repository

    async def sign_in(self, user: UserSignDTO) -> Token:
        db_user = await self._user_repository.get_by_username(user.username)
        if db_user is None:
            raise NotFound("Not user found")

        password = UserPassword(db_user.password)
        if not password.verify(user.password):
            raise BadRequest("Invalid password")

        
