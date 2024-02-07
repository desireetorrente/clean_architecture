# DTO to represent a note
# Serialize and deserialize a note
from dataclasses import dataclass


@dataclass(frozen=True)
class NoteDTO:
    id: str
    title: str
    description: str
    done: bool
