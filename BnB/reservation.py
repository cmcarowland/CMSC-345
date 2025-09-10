from datetime import datetime, timedelta
from typing import Optional

class Payment:
    ID = 0
    def generate_id():
        Payment.ID += 1
        return Payment.ID

    def __init__(
        self,
        reservationID: int,
        guaranteeExpiry: datetime,
        guaranteeAmount: float,
        fullAmount: float,
    ):
        self.paymentID = Payment.generate_id()
        self.reservationID = reservationID
        self.guaranteePaid = False
        self.guaranteeExpiry = guaranteeExpiry
        self.guaranteeAmount = guaranteeAmount
        self.fullAmount = fullAmount
        self.fullPaid = False

    def PayGuarentee(self, amount: float) -> None:
        if not self.guaranteePaid and amount >= self.guaranteeAmount:
            self.guaranteePaid = True

    def PayCheckout(self, amount: float) -> None:
        if not self.fullPaid and amount >= self.fullAmount:
            self.fullPaid = True

    def __repr__(self):
        return (
            f"Payment(paymentID={self.paymentID}, reservationID={self.reservationID}, "
            f"guaranteePaid={self.guaranteePaid}, guaranteeExpiry={self.guaranteeExpiry}, "
            f"guaranteeAmount={self.guaranteeAmount}, fullAmount={self.fullAmount}, "
            f"fullPaid={self.fullPaid})"
        )

class Reservation:
    ID = 0
    def generate_id():
        Reservation.ID += 1
        return Reservation.ID
    
    RoomTypes = {
        0: 200.0,
        1: 175.0,
        2: 120.0
    }

    def __init__(
        self,
        guestID: int,
        reservationStart: datetime,
        reservationEnd: datetime,
        roomID: int
    ):
        self.reservationID = Reservation.generate_id()
        self.guestID = guestID
        self.reservationStart = reservationStart
        self.reservationEnd = reservationEnd
        self.roomID = roomID
        self.closed = False
        gPayDate = reservationStart - timedelta(days=5)
        totalAmount = Reservation.RoomTypes[roomID] * (reservationEnd - reservationStart).days
        self.payment = Payment(self.reservationID, gPayDate, totalAmount * 0.25, totalAmount)

    def __repr__(self):
        return (
            f"Reservation(reservationID={self.reservationID}, guestID={self.guestID}, "
            f"payment={self.payment}, reservationStart={self.reservationStart}, "
            f"reservationEnd={self.reservationEnd}, roomID={self.roomID}, closed={self.closed})"
        )