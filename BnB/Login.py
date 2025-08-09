from textual.app import ComposeResult
from textual.containers import HorizontalGroup, VerticalGroup
from textual.widgets import (
    Button,
    Input,
    Label,
    MaskedInput
)


class Login(VerticalGroup):

    def compose(self) -> ComposeResult:
        yield HorizontalGroup(
            Label("User Name"),
            Input(placeholder="")
        )
        
        yield HorizontalGroup(
            Label("Password"),
            Input(
                "",
                tooltip="Obviously not your real credit card!",
                password=True
            )
        )

        yield HorizontalGroup(
            Button('Login', id='login'),
            Button('Create User', id='create'),
            Button('Quit', id='quit')
        )