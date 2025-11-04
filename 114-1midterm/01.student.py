'''
題目 1：類別與物件建立
請建立一個名為 `Student` 的類別，具備 `name` 和 `scores` 屬性，並加入 `average()` 方法，回傳三科平均。
'''
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
