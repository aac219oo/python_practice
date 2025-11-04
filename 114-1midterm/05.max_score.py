class Student:

    def __init__(self, name, scores) -> None:
        self.name = name
        self.scores = scores

    def average(self):
        ave = sum(self.scores) / len(self.scores)
        return ave


students = [
    Student("AA", [30, 50, 100]),
    Student("BB", [50, 100, 70]),
    Student("CC", [80, 90, 70])
]
top_student = max(students, key=lambda s: s.average())
print(f"平均分數最高的學生是{top_student.name}，最高平均分數為{top_student.average()}分")