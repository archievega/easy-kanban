from dataclasses import dataclass
from uuid import UUID


@dataclass(slots=True)
class Stage:
    ...

@dataclass(slots=True)
class Board:
    id: UUID
    name: str
    description: str
    stages: list[Stage]
