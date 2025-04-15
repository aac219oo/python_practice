numberList = []
primeNumberList = []

inputNum = int(input("數字1："))
inputNum2 = int(input("數字2："))
numberList.append(inputNum)
numberList.append(inputNum2)
def isPrimeNumber(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    
    for i in range(3, num):
        if num % i == 0:
            return False
    return True

def calPrimeNumberMul(x, y):
    for i in range(x, y + 1):
        if isPrimeNumber(i):
            primeNumberList.append(i)
    return primeNumberList
for number in calPrimeNumberMul(numberList[0], numberList[1] + 1):
    if number == primeNumberList[-1]:
        print(number, end="")
    else:
        print(number, end="+")


