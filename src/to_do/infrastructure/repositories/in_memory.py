import uuid
from ...application.interfaces import Repository
from ...application.dtos import NoteDTO


class NoteRepository(Repository[NoteDTO, str]):
    _notes = {}

    def generate_id(self) -> str:
        return str(uuid.uuid4())

    def add(self, obj: NoteDTO) -> None:
        self._notes[obj.id] = obj

    def get(self, obj_id: str) -> NoteDTO:
        return self._notes[obj_id]

    def remove(self, obj: NoteDTO) -> None:
        self._notes.pop(obj.id)

    def update(self, obj: NoteDTO) -> None:
        # refactor this
        self._notes[obj.id].update(obj)
