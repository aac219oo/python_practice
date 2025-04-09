'''
images\113-2midterm\calLeapYears.jpg
第3題
請設計一程式，能將使用者輸入之二個西元年份之間的閏年列出，並計算
閏年的個數有多少，依下列條件計算分數。

1.使用者能輸入兩個年份
2.設定一個判斷是否為閏年
3.印出閏年以及計算個數

閏年：每四年一次，第一百年不是，第四百年是
'''

inputFirstYear = int(input("請輸入第1個年份："))
inputSecondYear = int(input("請輸入第2個年份："))
yearsContainer = [inputFirstYear, inputSecondYear]
leapYaerCount = 0
leapYaersContainer = []

def isAD(year):
    if year > 0:
        return True
    else:
        return False

def isLeapYearFn(year):
    message = []
    if isAD(year):
        isLeapYear = year % 4 == 0 and year % 100 != 0 or year % 400 == 0
        if isLeapYear == True:
            message = [isLeapYear, "是"]
        else:
            message = [isLeapYear, "不是"]
        return message
    else:
        message = [False, "請輸入正確年分"]
        return message

for i in range(len(yearsContainer)):
    if isAD(yearsContainer[i]):
        print(f"西元{yearsContainer[i]}年{isLeapYearFn(yearsContainer[i])[1]}閏年")
    else:
        print(f"第{(i + 1)}個年份非西元後，{isLeapYearFn(yearsContainer[i])[1]}")

if isAD(inputFirstYear) & isAD(inputSecondYear):
    for i in range(inputFirstYear, inputSecondYear + 1):
            if isLeapYearFn(i)[0]:
                leapYaersContainer.append(i)
                leapYaerCount += 1
    print(f"西元{inputFirstYear}年到西元{inputSecondYear}年之間，{leapYaersContainer}為閏年")
    print(f"西元{inputFirstYear}年到西元{inputSecondYear}年總共有{leapYaerCount}個閏年")


