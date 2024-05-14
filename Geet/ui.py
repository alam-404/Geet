from prompt_toolkit.shortcuts import radiolist_dialog
from prompt_toolkit.styles import Style
from typing import TypeVar
from prompt_toolkit.application import Application
from prompt_toolkit.formatted_text import HTML


_T = TypeVar("_T")


class Dialog:
    def __init__(self) -> None:
        pass

    # Create a radio selection menu
    def radio_select(self, data: tuple) -> Application[_T]:
        style = Style.from_dict(
            {"radio-selected": "bg:#fff300", "radio-checked": "#0000e5"}
        )
        select = radiolist_dialog(
            title="Songs",
            text=HTML(
                "<b>Select the song</b>\n\u2191 Up \u2193 Down\nEnter - to select song\nTab - to select button"
            ),
            values=data,
            ok_text="Play",
            cancel_text="Exit",
            style=style,
        )
        return select
