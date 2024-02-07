from typing import Any
from .application.commands import Command, AddNoteComand
from .application.handlers import AddNoteHandler
from .infrastructure.repositories.in_memory import NoteRepository

note_repository = NoteRepository()

handlers = {AddNoteComand.__name__: AddNoteHandler(note_repository)}


class Dispatcher:
    _handlers = handlers

    def dispatch(self, command: Command) -> Any:
        try:
            handler = self._handlers[command.__class__.__name__]
        except KeyError:
            raise Exception("Handler not found")

        return handler.handle(command)
