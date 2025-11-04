'''
題目 4：抽象類別與多型
請定義抽象類別 `Animal`，並由 `Dog`、`Cat` 繼承後各自實作 `speak()` 方法。
'''
from abc import ABC, abstractmethod


class Animal(ABC):

    def __init__(self, type) -> None:
        self.type = type

    @abstractmethod
    def speak(type):
        pass


class Dog(Animal):

    def speak(self):
        return print(f"{self.type}汪汪叫")


class Cat(Animal):

    def speak(self):
        return print(f"{self.type}喵喵叫")


animals = [Dog("馬爾濟斯"), Cat("玳瑁貓")]
for animal in animals:
    animal.speak()
