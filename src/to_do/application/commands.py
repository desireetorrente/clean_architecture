from abc import ABC
from dataclasses import dataclass
from typing import Optional


class Command(ABC):
    ...

@dataclass
class AddNoteComand(Command):
    title: str
    description: str
    done: Optional[bool] = False
