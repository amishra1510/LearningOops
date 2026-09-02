from abc import ABC, abstractmethod


class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass


class UPI(Payment):
    def pay(self, amount):
        print(f"Paid ₹{amount} using UPI")


class Card(Payment):
    def pay(self, amount):
        print(f"Paid ₹{amount} using Card")


payments = [UPI(), Card()]

for payment in payments:
    payment.pay(500)
