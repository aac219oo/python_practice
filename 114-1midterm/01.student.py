class Student:

    def __init__(self, name, scores) -> None:
        self.name = name
        self.scores = scores

    def average(self):
        ave = sum(self.scores) / len(self.scores)
        return ave
stuA = Student("AA",[40,50,60])
result = stuA.average()
print(f"學生{stuA.name}的平均分數為{result}分")