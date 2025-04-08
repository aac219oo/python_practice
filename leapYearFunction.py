
year = int(input("年份："))

def learYear(yy):
    #isLeadYear = yy%4 == 0 and yy%100 != 0 or yy%400 ==0
    if (yy%4 == 0 and yy%100 != 0 or yy%400 ==0):
        return True
    else:
        return False

if learYear(year):
    print("是閏年")
else:
    print("不是閏年")

calLeadYear = 0

for i in range(1, year + 1):
    if learYear(i):
        calLeadYear += 1

print(calLeadYear)
