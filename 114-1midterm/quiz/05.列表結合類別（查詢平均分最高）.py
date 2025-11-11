class Employee:

    def __init__(self, name, department, salary) -> None:
        self.name = name
        self.department = department
        self.salary = salary

    def average(self):
        sum = 0
        ave = 0
        for i in employees:
            sum += i.salary
            ave = sum / len(employees)
        return ave


employees = [
    Employee("傑森", "資訊部門", 60000),
    Employee("喬伊", "會計部門", 35000),
    Employee("柔伊", "會計部門", 36000),
    Employee("勒布朗", "資訊部門", 75000),
    Employee("齊勒斯", "資訊部門", 85000),
    Employee("伊森", "會計部門", 40000),
]
top_salary_department = max(employees, key=lambda s: s.average())
top_salary = max(employees, key=lambda s: s.salary)
print(f"平均薪資最高的部門是{top_salary_department.department}，最高薪資為{top_salary.name}")

