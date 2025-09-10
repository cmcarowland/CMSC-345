import datetime
from BnB.calendar import Calendar
from BnB.reservation import Reservation

from textual.screen import Screen
from textual.app import App, ComposeResult
from textual.containers import VerticalGroup, Grid
from textual.validation import Function
from textual import on
import re
from textual.widgets import (
    Button,
    Input,
    Label,
    ListView,
    ListItem
)

class CreateReservation(Screen):
    def __init__(self):
        super().__init__()
        self.calendar = Calendar()

    def compose(self) -> ComposeResult:
        with VerticalGroup():
            with Grid(classes="label_input"):
                yield Label("Start Date")
                def date_validator(value):
                    return re.match(r'^\d{4}-[0-1][0-9]-[0-3][0-9]$', value) is not None

                yield Input(
                    id='start_date',
                    placeholder="Enter Start Date (YYYY-MM-DD)",
                    validate_on=["blur"],
                    validators=[Function(date_validator,  "Date must be in YYYY-MM-DD format")]

                )


            with Grid(classes="label_input"):
                yield Label("End Date")
                yield Input(
                    id='end_date',
                    placeholder="Enter End Date (YYYY-MM-DD)",
                    validators=[Function(date_validator,  "Date must be in YYYY-MM-DD format")]
                )

        yield ListView(
            ListItem(Label("Room With Bathroom")),
            ListItem(Label("Room with view")),
            ListItem(Label("Standard Room")),
        )

        with Grid(classes='login_button_group'):
            yield Button('Create', id='create')
            yield Button('Cancel', id='cancel')

    def on_button_pressed(self, event: Button.Pressed) -> None:
        button_id = event.button.id
        if button_id == 'cancel':
            self.dismiss()
        elif button_id == 'create':
            try:
                start_date_str = self.query_one('#start_date').value
                end_date_str = self.query_one('#end_date').value
                if not start_date_str or not end_date_str:
                    self.notify("Start date and end date must be provided", severity="error", timeout=5)
                    return

                start_date = datetime.datetime.strptime(start_date_str, "%Y-%m-%d")
                end_date = datetime.datetime.strptime(end_date_str, "%Y-%m-%d")
                if start_date >= end_date:
                    self.notify("End date must be after start date", severity="error", timeout=5)
                    return

                selected_room = self.query_one(ListView).index
                if selected_room is None:
                    self.notify("Please select a room type", severity="error", timeout=5)
                    return

                room_id = selected_room  # Assuming room IDs are 0, 1, 2 for the three types

                reservation = Reservation(guestID=1, reservationStart=start_date, reservationEnd=end_date, roomID=room_id)
                self.calendar.add_reservation(reservation)
                self.notify(f"Reservation {reservation.reservationID} created successfully!", severity="success", timeout=5)
            except ValueError as ve:
                self.notify(str(ve), severity="error", timeout=5)
            except Exception as e:
                self.notify(f"Error creating reservation: {str(e)}", severity="error", timeout=5)

    @on(Input.Blurred)
    def show_invalid_reasons(self, event: Input.Blurred) -> None:
        # Show a toast notification for invalid input
        if not event.validation_result.is_valid:
            self.notify("\n".join(event.validation_result.failure_descriptions), severity="error", timeout=5)
