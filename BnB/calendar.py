import datetime
from BnB.reservation import Reservation

import os

class Calendar:
    def __init__(self):
        self.reservations = []
        if os.path.exists("reservations.txt"):
            with open("reservations.txt", "r") as f:
                for line in f:
                    parts = line.strip().split(",")
                    if len(parts) == 5:
                        reservationID = int(parts[0])
                        guestID = int(parts[1])
                        reservationStart = datetime.strptime(parts[2], "%Y-%m-%d")
                        reservationEnd = datetime.strptime(parts[3], "%Y-%m-%d")
                        roomID = int(parts[4])
                        reservation = Reservation(guestID, reservationStart, reservationEnd, roomID)
                        reservation.reservationID = reservationID
                        self.reservations.append(reservation)

    def add_reservation(self, reservation):
        for r in self.reservations:
            if (r.roomID == reservation.roomID and (
                reservation.reservationEnd >= r.reservationStart or
                reservation.reservationStart <= r.reservationEnd)):
                raise ValueError("Reservation dates overlap with an existing reservation.")
        
        self.reservations.append(reservation)

    def remove_reservation(self, reservation):
        if reservation in self.reservations:
            self.reservations.remove(reservation)

    def get_reservations(self):
        return self.reservations
