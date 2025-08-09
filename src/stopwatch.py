from textual.app import App, ComposeResult
from textual.containers import HorizontalGroup, VerticalScroll
from textual.widgets import Footer, Header, Button, Digits

class TimeDisplay(Digits):
    '''A widget to display time'''

class StopWatch(HorizontalGroup):

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "start":
            self.add_class("started")
        elif event.button.id == "stop":
            self.remove_class("started")

    def compose(self):
        yield Button('Start', id='start', variant='success')
        yield Button('Stop', id='stop', variant='error')
        yield Button('Reset', id='reset')
        yield TimeDisplay("00:00:00.00")

class StopWatchApp(App):

    CSS_PATH = "stopwatch.css"
    BINDINGS = [('d', 'toggle_dark', 'Toggle Dark Mode')]

    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()
        yield VerticalScroll(StopWatch(), StopWatch(), StopWatch())

    def action_toggle_dark(self) -> None:
        print("Called")
        self.theme = ('textual-dark' if self.theme == 'textual-light' else 'textual-light')


if __name__ == "__main__":
    app = StopWatchApp()
    app.run()