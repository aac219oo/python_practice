class Employee:

    def __init__(self, name) -> None:
        self.name = name

    def cal_salary(self):
        return 0

    def show_info(self):
        print(f"員工 {self.name}: 這個月的薪水是{self.cal_salary()}元")


class Fulltime_Employee(Employee):

    def __init__(self, name, base_salary) -> None:
        super().__init__(name)
        self.__salary = base_salary
        self.__bonus = 0

    def add_bonus(self, bonus):
        if self.__salary >= bonus >= 0:
            self.__bonus = bonus
        else:
            print("獎金不符合規定！")

    def cal_salary(self):
        return self.__salary + self.__bonus


class Parttime_Employee(Employee):

    def __init__(self, name, hourly_rate, hours_worked) -> None:
        super().__init__(name)
        self.__hourly_rate = hourly_rate
        self.__hours_worked = hours_worked

    def set_hourly_rate(self, hourly_rate):
        if 250 >= hourly_rate >= 190:
            self.__hourly_rate = hourly_rate
        else:
            print("時薪不符合規定！")

    def set_hours_worked(self, hours_worked):
        if 168 >= hours_worked >= 0:
            self.__hours_worked = hours_worked
        else:
            print("工作時數不符合規定！")

    def cal_salary(self):
        return self.__hourly_rate * self.__hours_worked


employees = [
    Fulltime_Employee("Jhonson", 40000),
    Fulltime_Employee("Joe", 30000),
    Parttime_Employee("Jhon", 250, 168),
    Parttime_Employee("Jojo", 200, 160)
]
employees[0].add_bonus(30000)
employees[1].add_bonus(20000)
employees[2].set_hourly_rate(260)
employees[2].set_hours_worked(200)
employees[2].set_hourly_rate(210)
employees[2].set_hours_worked(168)
for employee in employees:
    employee.show_info()
