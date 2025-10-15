class Employee:

    def __init__(self, name, base_salary) -> None:
        self.name = name
        self.__salary = base_salary
        self.__bonus = 0

    def set_bonus(self, bonus):
        if 0 <= bonus <= self.__salary:
            self.__bonus = bonus
        else:
            print("獎金不符合規定！")

    def get_salary(self):
        return self.__salary + self.__bonus


stu1 = Employee("陳大大", 40000)
stu1.set_bonus(80)
print(stu1.get_salary())
