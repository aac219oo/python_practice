'''
images\113-2midterm\calIntMultiple.jpg
第5题
試撰寫一個程式，讓使用者輸入1~15之間的整數後，計算出1至100之此
數倍數的個數。
例如:
輸入6，即計算1~100之間，所有6倍數的個數。
輸入9，即計算1~100之間，所有9倍數的個數。
'''

number = int(input("請輸入1~15其中一個整數："))

limit = 100
mulCount = 0
isRange = False
isMultiple = False

if 1 <= number <= 15:
    isRange = True
else:
    print("請輸入1~15的正整數")

for i in range(1, limit + 1):
    #print(i, i % number)
    if isRange:
        isMultiple = i % number == 0
        if isMultiple:
            mulCount += 1
if isRange:
    print(f"即計算1~100之間，所有{number}的倍數有{mulCount}個")
