'''
題目 3：繼承基本練習
請建立 `Person` 父類別與 `Teacher` 子類別，並顯示老師的名字與科目。
'''
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
