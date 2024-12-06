import jwt

from src.domain.entities.jwt import PayloadDTO, TokenDTO
from src.main.config import settings


class JWTService:
    def __init__(self):
        self.access_token = settings.JWT_ACCESS_TOKEN
        self.refresh_token = settings.JWT_REFRESH_TOKEN
        self.expiration_time = settings.JWT_EXPIRATION_TIME

    def decode(self, token, token_type: str = 'access') -> PayloadDTO:
        return jwt.decode(token,
                          self.access_token if token_type == 'access' else self.refresh_token,
                          algorithms=['HS256']
                          )

    def encode(self, payload: PayloadDTO, token_type: str = 'access') -> TokenDTO:
        return TokenDTO(
            token=jwt.encode(
                payload=payload,
                key=self.access_token if token_type == 'access' else self.refresh_token,
                algorithm=settings.JWT_ALGORITHM
            )
        )
