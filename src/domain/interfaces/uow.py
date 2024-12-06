from typing import Protocol


class UoW(Protocol):
    def commit(self) -> None:
        ...

    def rollback(self) -> None:
        ...

    def flush(self) -> None:
        ...
