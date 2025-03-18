year = int(input("年份："))

isLeadYear = year%4 == 0 and year%100 != 0 or year%400 ==0

if isLeadYear:
    print("是閏年")
else:
    print("不是閏年")

calLeadYear = 0

for i in range(1, year + 1):
    if i%4 == 0 and i%100 != 0 or i%400 ==0:
        calLeadYear += 1

print(calLeadYear)
