from textual.app import App, ComposeResult
from textual.containers import HorizontalGroup, VerticalGroup, Grid
from textual.widgets import (
    Button,
    Input,
    Label,
)

class Login(VerticalGroup):
    CSS_PATH = 'Login.tcss'

    def compose(self) -> ComposeResult:
        with Grid(classes="label_input"):
            yield Label("User Name")
            yield Input(placeholder="")
        
        with Grid(classes="label_input"):
            yield Label("Password")
            yield Input(
                "",
                tooltip="Obviously not your real credit card!",
                password=True
            )

        with Grid(id='login_button_group'):
            yield Button('Login', id='login')
            yield Button('Create User', id='create')
            yield Button('Quit', id='quit')

    def on_button_pressed(self, event: Button.Pressed) -> None:
        button_id = event.button.id
        if button_id == 'quit':
            self.app.exit()
