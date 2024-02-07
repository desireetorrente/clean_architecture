from abc import ABC, abstractmethod
from .commands import AddNoteComand, Command
from .interfaces import Repository
from ..domain.model import Note, NoteId, NoteTitle, NoteDescription, NoteDone
from .dtos import NoteDTO


class Hander(ABC):
    @abstractmethod
    def handle(self, command: Command) -> None:
        pass


class AddNoteHandler(Hander):
    def __init__(self, repository: Repository) -> None:
        self.repository = repository

    def handle(self, command: AddNoteComand) -> NoteDTO:
        # validate busness rules
        note = Note(
            id=NoteId.from_string(self.repository.generate_id()),
            title=NoteTitle(command.title),
            description=NoteDescription(command.description),
            done=NoteDone(command.done),
        )

        # TODO: Add DTO serializer
        self.repository.add(
            NoteDTO(
                str(note.id.value),
                note.title.value,
                note.description.value,
                note.done.value,
            )
        )

        # Only for testing purposes
        return self.repository.get(str(note.id.value))
