import sqlalchemy as sa
from sqlalchemy.orm import Mapped
from sqlalchemy.testing.schema import mapped_column

from src.adapters.database.config import Base


class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(sa.Integer, primary_key=True)
    username: Mapped[str] = mapped_column(sa.String(255), unique=True, index=True)
    password: Mapped[str] = mapped_column(sa.String(255), index=True)
