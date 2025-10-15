class Student:

    def __init__(self, name) -> None:
        self.name = name
        self.__score = 0

    def set_score(self,score):
        if 0 <= score <= 100:
           self.__score = score
        else:
            print("成績輸入錯誤，請輸入0到100之間的分數")

    def get_score(self):
        return self.__score


stu1 = Student("陳大大")
stu1.set_score(80)
print(stu1.get_score())