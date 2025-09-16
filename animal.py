class Animal:

    def __init__(self, name, color, owner) -> None:
        self.name = name
        self.color = color
        self.owner = owner

    def walk(self):
        print(self.name + "正在走路")
    def make_sound(self):
        print(self.name + "正在發出聲音")


class Cat(Animal):

    def __init__(self, name, color, owner) -> None:
        self.name = name
        self.color = color
        self.owner = owner
    def make_sound(self):
        print(self.name + "正在喵喵叫")


class Dog(Animal):

    def __init__(self, name, color, owner) -> None:
        self.name = name
        self.color = color
        self.owner = owner
    def make_sound(self):
        print(self.name + "正在旺旺叫")


class Pig(Animal):

    def __init__(self, name, color, owner) -> None:
        self.name = name
        self.color = color
        self.owner = owner

    def make_sound(self):
        print(self.name + "正在齁齁叫")

myPet1 = Cat("money", "silver", "James")
myPet2 = Dog("小黑", "black", "Peter")
myPet3 = Pig("佩琪", "pink", "Mei")
myPet1.make_sound()
myPet2.make_sound()
myPet3.make_sound()