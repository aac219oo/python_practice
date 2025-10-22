# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
class Employee: #父類別
    def __init__(self, name):
        self.name = name

    def calculate_salary(self):
        return 0  # 父類別預設薪資為 0

    def show_info(self):
        print(f"{self.name} 的薪資為：{self.calculate_salary()} 元")


class FullTimeEmployee(Employee):
    def __init__(self, name, base_salary):
        super().__init__(name)
        self.__base_salary = base_salary
        self.__bonus  = 5000  # 外島、專業能力津貼

    def set_base_salary(self, salary): #修改基本薪資
        if salary >= 0:
            self.__base_salary = salary

    def get_base_salary(self): #取得基本薪資
        return self.__base_salary

    def calculate_salary(self):
        return self.__base_salary + self.__bonus


class PartTimeEmployee(Employee):
    def __init__(self, name, hourly_rate, hours_worked):
        super().__init__(name)
        self.__hourly_rate = hourly_rate
        self.__hours_worked = hours_worked

    def set_hours(self, hours):
        if hours >= 0:
            self.__hours_worked = hours

    def get_hours(self):
        return self.__hours_worked

    def calculate_salary(self):
        return self.__hourly_rate * self.__hours_worked


# === 主程式 ===

employees = [
    FullTimeEmployee("王明明", 35000),
    FullTimeEmployee("林曉曉", 42000),
    PartTimeEmployee("陳廷廷", 200, 80),
    PartTimeEmployee("李蓉蓉", 180, 60)
]

employees[0].set_base_salary(37000)
employees[1].set_base_salary(32000)


print(">>公司薪資報表：")
for emp in employees:
    emp.show_info()