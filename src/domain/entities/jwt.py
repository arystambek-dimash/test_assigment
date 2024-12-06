from dataclasses import dataclass


@dataclass
class TokenDTO:
    token: str


@dataclass
class PayloadDTO:
    user_id: int
