from textual.app import App, ComposeResult
from textual.widgets import Footer, Header

class StopWatchApp(App):
    BINDINGS = [('d', 'toggle_dark', 'Toggle Dark Mode')]

    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()

    def action_toggle_dark(self) -> None:
        print("Called")
        self.theme = ('textual-dark' if self.theme == 'textual-light' else 'textual-light')


if __name__ == "__main__":
    app = StopWatchApp()
    app.run()