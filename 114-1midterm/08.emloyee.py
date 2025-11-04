'''
設計 `Employee` 類別，其薪資為私有屬性，並透過 setter 限制最低薪資不得低於 26400 元（基本工資）。
'''

class Employee:

    def __init__(self, name) -> None:
        self.name = name

    def cal_salary(self):
        return 0

    def show_info(self):
        print(f"員工 {self.name}: 這個月的薪水是{self.cal_salary()}元")


class Fulltime_Employee(Employee):

    def __init__(self, name, salary) -> None:
        super().__init__(name)
        self.__salary = salary

    def cal_salary(self):
        if self.__salary >= 26400:
            return self.__salary
        else:
            print(f"{self.name}最低薪資不得低於 26400 元（基本工資）")
            return 26400



employees = [
    Fulltime_Employee("Jhonson", 40000),
    Fulltime_Employee("Joe", 20000),
]
for employee in employees:
    employee.show_info()
