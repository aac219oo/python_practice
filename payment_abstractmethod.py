from abc import ABC, abstractmethod


class PaymentMethod(ABC):

    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

    @abstractmethod
    def pay(amount):
        pass


class CreditCardPayment(PaymentMethod):

    def pay(self):
        return self.amount * 1.05


class CashPayment(PaymentMethod):

    def pay(self):
        return self.amount


class LinePayPayment(PaymentMethod):

    def pay(self):
        return self.amount - 10


payment = [
    CreditCardPayment("JJ", 500),
    CashPayment("Jolin", 600),
    LinePayPayment("Jay", 700)
]
for p in payment:
    print(f"{p.name}應付：{p.pay()}元")
