'''
images\113-2midterm\parkingFee.jpg
第2题
請設計一程式能支援使用者輸入二個小於20的正整數，並依數字大小印出
圖形。例如使用者輸入4,8，則印出4x8的*字元形成之矩形。

請輸入數字A:4
請輸入數字B:8
********
********
********
********
'''

inputHeight = int(input("請輸入長度："))
inputWeight = int(input("請輸入寬度："))

if 0 < inputWeight < 20 and 0 < inputWeight < 20:
    for i in range(inputHeight):
        for ii in range(inputWeight):
            print("*", end="")
        print("")
else:
    print("請輸入小於20的正整數")