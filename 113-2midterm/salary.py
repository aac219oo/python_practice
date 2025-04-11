'''
images\113-2midterm\salary.jpg
第7题
小蔡在Toyota公司上班，薪水包括底薪和加成、業績獎金。底薪為16,855
元，獎金則是依照銷售車輛來計算。請撰寫一程式，提示使用者輸入銷售
量，然後算出小明該領的薪水總額。
例如:小蔡賣出20台，薪水共有16855+(16855*0.3)+50000=71912
    小蔡賣出46台，16855+(16855*0.5)+100000+(6*5000)=155283
'''
import math
from decimal import Decimal, ROUND_HALF_UP
basicSalary = 16855

# inputSellCarsCount = int(input("請輸入這個月賣了幾台車："))
# def calSalary(count):
#     if count < 5:
#         salary = basicSalary
#     elif 5 <= count < 10:
#         salary = basicSalary + (basicSalary * 0.1) + 5000
#     elif 10 <= count < 20:
#         salary = basicSalary + (basicSalary * 0.2) + 10000
#     elif 20 <= count < 40:
#         salary = basicSalary + (basicSalary * 0.3) + 50000
#     elif count >= 40:
#         salary = basicSalary + (basicSalary * 0.5) + 100000 + ((count - 40)*5000)
#     return salary

# print(f"小蔡這個月薪水為{math.ceil(calSalary(inputSellCarsCount))}元")

extraBonusRules = [
    {"min": 0, "max": 5, "rate": 0, "bonus": 0, "extra": 0},
    {"min": 5, "max": 10, "rate": 0.1, "bonus": 5000, "extra": 0},
    {"min": 10, "max": 20, "rate": 0.2, "bonus": 10000, "extra": 0},
    {"min": 20, "max": 40, "rate": 0.3, "bonus": 50000, "extra": 0},
    {"min": 40, "max": float('inf'), "rate": 0.5, "bonus": 100000, "extra": 5000}
]

while True:
    try:
        inputSellCarsCount = int(input("請輸入這個月賣了幾台車："))
        if inputSellCarsCount >= 0:
            break
        else:
            print("請勿小於0")
    except ValueError:
        print("請輸入正整數")

def calSalary(count):
    for i in range(len(extraBonusRules)):
        if extraBonusRules[i]["min"] <= count < extraBonusRules[i]["max"]:
            salary = basicSalary + (basicSalary * extraBonusRules[i]["rate"]) + extraBonusRules[i]["bonus"] + ((count - 40) * extraBonusRules[i]["extra"])
            break
    return salary

print(f"小蔡這個月薪水為{math.ceil(calSalary(inputSellCarsCount))}元")
print(Decimal(str(calSalary(inputSellCarsCount))).quantize(Decimal('1'), rounding=ROUND_HALF_UP))