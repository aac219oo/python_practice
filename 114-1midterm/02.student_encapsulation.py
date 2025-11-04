'''
題目 2：封裝與成績設定
請建立一個名為 `Student` 的類別，在 `Student` 類別中將 `scores` 設為私有屬性，
並使用 `set_scores()` 方法來設定，若分數不是 0~100，則拒絕設定。
'''
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
