from abc import ABC, abstractmethod


class Operation(ABC):

    def __init__(self, a, b):
        self.a = a
        self.b = b

    @abstractmethod
    def compute(a, b):
        pass


class Add(Operation):

    def compute(self):
        return self.a + self.b


class Subtract(Operation):

    def compute(self):
        return self.a - self.b


class Multiply(Operation):

    def compute(self):
        return self.a * self.b

class Divide(Operation):

    def compute(self):
        return self.a // self.b


result = [
    Add(400, 500),
    Subtract(700, 600),
    Multiply(50, 70),
    Divide(1200, 600),
]
for r in result:
    print(f"{r.compute()}")
