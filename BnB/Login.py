from hashlib import md5

from BnB.utils import get_users, save_users
from BnB.Create import Create

from textual.screen import Screen
from textual.app import App, ComposeResult
from textual.containers import VerticalGroup, Grid
from textual.widgets import (
    Button,
    Input,
    Label,
)

class Login(Screen):
    CSS_PATH = 'styles.tcss'

    def check_login(self) -> bool:
        users = get_users()
        username = self.query_one('#username').value
        password = md5(self.query_one('#password').value.encode()).hexdigest()
        if users.get(username) == password:
            return True
        
        return False

    def compose(self) -> ComposeResult:
        with VerticalGroup():
            with Grid(classes="label_input"):
                yield Label("User Name")
                yield Input(id='username', placeholder="")

            with Grid(classes="label_input"):
                yield Label("Password")
                yield Input(
                    id='password',
                    placeholder="Enter Password",
                    tooltip="Obviously not your real credit card!",
                    password=True
                )

        with Grid(classes='login_button_group'):
            yield Button('Login', id='login')
            yield Button('Create User', id='create')
            yield Button('Quit', id='quit')

    def on_button_pressed(self, event: Button.Pressed) -> None:
        button_id = event.button.id
        if button_id == 'quit':
            self.app.exit()
        elif button_id == 'create':
            self.app.push_screen(Create())
        elif button_id == 'login':
            if self.check_login():
                self.notify("Login Successful!!", severity="success", timeout=5)
            else:
                self.notify("Invalid username or password", severity="error", timeout=5)
