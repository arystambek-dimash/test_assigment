from datetime import timedelta
from functools import lru_cache

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DB_NAME: str
    DB_USER: str
    DB_PASS: str
    DB_HOST: str
    DB_PORT: int

    JWT_ACCESS_TOKEN: str
    JWT_REFRESH_TOKEN: str
    JWT_ACCESS_EXPIRATION_DELTA: timedelta
    JWT_REFRESH_EXPIRATION_DELTA: timedelta

    @property
    def get_db_url(self):
        return f"asyncpg+postgresql://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"


@lru_cache
def get_settings():
    return Settings()


settings = get_settings()
