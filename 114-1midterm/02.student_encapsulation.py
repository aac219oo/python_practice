class Student:

    def __init__(self, name) -> None:
        self.name = name
        self.__score = 0

    def set_scores(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            print("成績輸入錯誤，請輸入0到100之間的分數")
    def get_score(self):
        return self.__score

stuA = Student("AA")
stuA.set_scores(90)
result = stuA.get_score()
print(f"學生{stuA.name}的分數為{result}分")
