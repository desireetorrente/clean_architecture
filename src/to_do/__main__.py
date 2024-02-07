from typing import Any, Dict
from to_do.application.commands import AddNoteComand
from to_do.dispatcher import Dispatcher

dispatcher = Dispatcher()


def add_note(data: Dict[str, Any]):
    command = AddNoteComand(**data)
    new_note = dispatcher.dispatch(command)

    print(new_note)


if __name__ == "__main__":
    add_note(
        {
            "title": "Test",
            "description": "This is a test",
        }
    )
