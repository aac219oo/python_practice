year = int(input("生肖年份："))

chineseZodiac = ["鼠", "牛", "虎", "兔", "龍", "蛇", "馬", "羊", "猴", "雞", "狗", "豬"]

baseYear = 4

index = (year - baseYear) % 12  
print(chineseZodiac[index])

'''
if ((year - baseYear)%12 == 0):
    print(chineseZodiac[0])
elif ((year - baseYear)%12 == 1):
    print(chineseZodiac[1])
elif ((year - baseYear)%12 == 2):
    print(chineseZodiac[2])
elif ((year - baseYear)%12 == 3):
    print(chineseZodiac[3])
elif ((year - baseYear)%12 == 4):
    print(chineseZodiac[4])
elif ((year - baseYear)%12 == 5):
    print(chineseZodiac[5])
elif ((year - baseYear)%12 == 6):
    print(chineseZodiac[6])
elif ((year - baseYear)%12 == 7):
    print(chineseZodiac[7])
elif ((year - baseYear)%12 == 8):
    print(chineseZodiac[8])
elif ((year - baseYear)%12 == 9):
    print(chineseZodiac[9])
elif ((year - baseYear)%12 == 10):
    print(chineseZodiac[10])
elif ((year - baseYear)%12 == 11):
    print(chineseZodiac[11])'
'''