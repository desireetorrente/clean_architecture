from dataclasses import dataclass
import uuid


@dataclass(frozen=True)
class NoteId:
    value: uuid.UUID

    @staticmethod
    def from_string(id: str):
        return NoteId(uuid.UUID(id))

    def __post_init__(self):
        if not isinstance(self.value, uuid.UUID):
            raise ValueError("Id should be a valid UUID")


@dataclass(frozen=True)
class NoteTitle:
    value: str

    def __post_init__(self):
        if len(self.value) < 3:
            raise ValueError("Title should be at least 3 characters long")


@dataclass(frozen=True)
class NoteDescription:
    value: str

    def __post_init__(self):
        if len(self.value) < 3:
            raise ValueError("Description should be at least 3 characters long")


@dataclass(frozen=True)
class NoteDone:
    value: bool

    def __post_init__(self):
        if not isinstance(self.value, bool):
            raise ValueError("Done should be a boolean")


class Note:
    _id: NoteId
    _title: NoteTitle
    _description: NoteDescription
    _done: NoteDone

    def __init__(self, id, title, description, done) -> None:
        self._id = id
        self._title = title
        self._description = description
        self._done = done

    @property
    def id(self):
        return self._id

    @property
    def title(self):
        return self._title

    @property
    def description(self):
        return self._description

    @property
    def done(self):
        return self._done

    def mark_as_done(self):
        self._done = NoteDone(True)
