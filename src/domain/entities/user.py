from pydantic.dataclasses import dataclass


@dataclass(frozen=True)
class UserDTO:
    id: int
    username: str
    password: str


@dataclass
class UserCrudDTO(UserDTO):
    username: str
    password: str


@dataclass(frozen=True)
class UserResponseDTO:
    id: int
    username: str
