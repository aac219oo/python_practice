height = float(input("請輸入身高(cm)："))
weight = float(input("請輸入體重(kg)："))

def calBmi(hh, ww):
    bmi = ww/((hh/100) ** 2)
    return round(bmi, 2)

print(calBmi(height, weight))