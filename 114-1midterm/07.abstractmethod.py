from abc import ABC, abstractmethod
'''
設計電子商店的商品類別與兩種產品，顯示描述與計算總價
'''

class Category(ABC):

    def __init__(self, name, context, price, amount):
        self.name = name
        self.context = context
        self.price = price
        self.amount = amount

    @abstractmethod
    def cal_total_price(price, amount):
        pass


class Paper(Category):

    def cal_total_price(self):
        return self.price * self.amount


class Doll(Category):

    def cal_total_price(self):
        return self.price * self.amount


cart = [
    Paper("A4紙","列印機用紙A4紙", 500, 5),
    Doll("娃娃", "可愛的布娃娃", 600, 1),
]
for i in cart:
    print(f"商品名稱：{i.name}，商品描述：{i.context}，商品數量：{i.amount}，總價：{i.cal_total_price()}元")
