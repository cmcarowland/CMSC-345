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


if __name__ == "__main__":
    app = MainMenu()
    app.run()