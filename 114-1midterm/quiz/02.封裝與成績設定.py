class Student:

    def __init__(self, name) -> None:
        self.name = name
        self.__scores = 0

    def set_scores(self, score):
        if 0 <= score <= 100:
            self.__scores = score
        else:
            print("成績輸入錯誤，請輸入0到100之間的分數")

    def get_level(self):
        if 100 >= self.__scores >= 90:
            return "優"
        elif 89 >= self.__scores >= 80:
            return "佳"
        elif 79 >= self.__scores >= 70:
            return "可"
        elif 69 >= self.__scores >= 0:
            return "平"


stuA = Student("James")
stuA.set_scores(100)
result = stuA.get_level()
print(f"學生{stuA.name}的表現{result}")
