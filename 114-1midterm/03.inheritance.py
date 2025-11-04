class Person:

    def __init__(self, name) -> None:
        self.name = name


class Teacher(Person):

    def __init__(self, name, subject) -> None:
        super().__init__(name)
        self.subject = subject

    def show_info(self):
        print(f"{self.name}老師教授的科目是{self.subject}")


teachers = [Teacher("陳大大", "數學")]
for teacher in teachers:
    teacher.show_info()