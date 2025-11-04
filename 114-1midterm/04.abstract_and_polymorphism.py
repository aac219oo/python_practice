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