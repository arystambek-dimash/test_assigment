from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase, sessionmaker

from src.main.config import settings

engine = create_async_engine(
    settings.get_db_url,
    echo=False,
    future=True,
)

AsyncSession = async_sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)


class Base(DeclarativeBase):
    pass
