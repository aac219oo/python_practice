from abc import ABC, abstractmethod

class Transport(ABC):

    def __init__(self, type) -> None:
        self.type = type

    @abstractmethod
    def cal_shipping_fee(type):
        pass


class Cars(Transport):
    def __init__(self, type, fee, amount) -> None:
        super().__init__(type)
        self.fee = fee
        self.amount = amount

    def cal_shipping_fee(self):
        return self.fee * self.amount


class Bikes(Transport):
    def __init__(self, type, fee, amount) -> None:
        super().__init__(type)
        self.fee = fee
        self.amount = amount

    def cal_shipping_fee(self):
        return self.fee * self.amount


transports = [Cars("豐田汽車", 1000, 5), Bikes("三陽機車", 200, 20)]
transports_count = 0
for transport in transports:
    print(f"{transport.type}的運費為{transport.cal_shipping_fee()}元")
    transports_count += transport.amount

print(f"統計共有{transports_count}台交通工具")
