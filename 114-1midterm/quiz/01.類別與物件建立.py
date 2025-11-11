subjects = ["國文","英文","數學"]

class Student:

    def __init__(self, name) -> None:
        self.name = name
        self.__scores = []

    def average(self):
        ave = sum(self.__scores) / len(self.__scores)
        result = round(ave, 2)
        return result
    
    def add_score(self, scores):
        for s in subjects:
            self.__scores = scores
    
    def display(self):
        subjectsStr = ','.join(str(s) for s in subjects)
        print(f"學生{self.name}科目{subjectsStr}平均分數為{self.average()}分")

student_list = [Student("AA"),Student("BB"),Student("CC"),]
student_list[0].add_score([30,50,60])
student_list[1].add_score([30,50,60])
student_list[2].add_score([30,50,60])
for student in student_list:
    student.display()