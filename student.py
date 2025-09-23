import random

class Student:
    def __init__(self, name, scores) -> None:
        self.name = name
        self.score_list = scores
    def avg(self):
        average = sum(self.score_list) / len(self.score_list)
        return average
    def is_passed(self):
        return self.avg() >= 60
    def show_scores(self):
        subjects = ["國文","英文","數學"]
        print(f"{self.name}的成績：")
        for i in range(3):
            print(f"{subjects[i], self.score_list[i]}分")
        print(f" >> 平均：{self.avg():.2f}分")
        print(f" >> 結果：{'及格' if self.is_passed() else '不及格'}")

# stuA = Student("AA",[40,50,60])
# stuA.show_scores()

student_list = []

n = int(input("請輸入學生人數："))


for i in range(n):
    keyin_name = input(f"請輸入第{i+1}位學生的姓名：")
    keyin_score_list = [random.randint(50, 90) for _ in range(3)]
    # for subject in ["國文","英文","數學"]:
    #     keyin_score = int(input(f"請輸入{subject}的成績："))
    #     keyin_score_list.append(keyin_score)
    stuNew = Student(keyin_name, keyin_score_list)
    student_list.append(stuNew)

#print(student_list)

passed_count = 0
print("\n學生成績報告：")
for stu in student_list:
    result = "及格" if stu.is_passed() else "不及格"
    print(f"{stu.name}:{stu.avg()}分，{result}")
    if stu.is_passed():
        passed_count += 1

failed_count = n - passed_count
print(f"\n統計結果：及格{passed_count}人，不及格{failed_count}人")

#找出學生中最高分數
top_student = max(student_list, key=lambda s: s.avg())
print(f"最高分學生：{top_student.name}，分數：{top_student.avg():.2f}")