from BnB.Login import Login

from textual.app import App, ComposeResult
from textual.widgets import Footer, Header, Button


class MainMenu(App):
    #BINDINGS = [('d', 'toggle_dark', 'Toggle Dark Mode')]
    TITLE = 'Bed And Breaky'
    CSS_PATH = 'styles.tcss'


    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()
        yield Login()

    # This must be named the message class name
    # def on_login_my_custom_message(self, message: Login.MyCustomMessage) -> None:
    #     """Handle the custom message from the Login component."""
    #     self.notify("It's a trap!", severity="error", timeout=10)
    #     # self.exit()


if __name__ == "__main__":
    app = MainMenu()
    app.run()