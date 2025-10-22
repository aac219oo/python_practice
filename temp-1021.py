# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# 題目：交通工具資訊系統（列表 + 繼承 + 抽象類別）
from abc import ABC, abstractmethod


class Vehicle(ABC): #抽象類別
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def get_info(self):
        pass


class Car(Vehicle):
    def __init__(self, name, seats):
        super().__init__(name)
        self.seats = seats

    def get_info(self):
        return f"汽車 {self.name} 可載 {self.seats} 人"


class Bike(Vehicle):
    def __init__(self, name, type):
        super().__init__(name)
        self.type = type
    def get_info(self):
        return f"腳踏車 {self.name} 是 {self.type} 類型"

vehicles = [
    Car("Toyota Corolla", 5),
    Bike("Giant ATX", "登山車"),
    Car("Tesla Model 3", 5),
    Bike("Merida RoadRace", "公路車")
        ]


for v in vehicles:
    print(v.get_info())