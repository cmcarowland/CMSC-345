from hashlib import md5
from BnB.utils import get_users, save_users
from textual.screen import ModalScreen
from textual.app import App, ComposeResult
from textual.containers import VerticalGroup, Grid
from textual.widgets import (
    Button,
    Input,
    Label,
)

class Create(ModalScreen):
    CSS_PATH = 'styles.tcss'

    def compose(self) -> ComposeResult:
        with VerticalGroup():
            with Grid(classes="label_input"):
                yield Label("User Name")
                yield Input(id='username', placeholder="Enter User Name")

            with Grid(classes="label_input"):
                yield Label("Password")
                yield Input(
                    id='password',
                    placeholder="Enter Password",
                    tooltip="Don't forget your password!",
                    password=True
                )

        with Grid(classes='login_button_group'):
            yield Button('Create', id='create')
            yield Button('Cancel', id='cancel')

    def on_button_pressed(self, event: Button.Pressed) -> None:
        button_id = event.button.id
        if button_id == 'cancel':
            self.dismiss()
        elif button_id == 'create':
            users = get_users()
            newUser = self.query_one('#username').value
            if newUser not in users:
                users[newUser] = md5(self.query_one('#password').value.encode()).hexdigest()
                save_users(users)
                self.dismiss()
            else:
                self.notify("User already exists!", severity="warning", timeout=5)
