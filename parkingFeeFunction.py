'''
1.每小時30元
2.滿半小時以1小時計
3.每日上限為300元
4.輸入停車分鐘數(整數)
'''

perHourFee = 30
perDaylimitFee = 300
parkingMin = int(input("請輸入總停車時間(分鐘)："))

def calParkingFee(min):
    calHour = min/60
    if min % 60 >= 30:
        calHour += 1
    totalFee = perHourFee * calHour
    if totalFee >= 300:
        totalFee = perDaylimitFee
    elif 1 <= parkingMin <= 60:
        totalFee = perHourFee

    return totalFee

print(calParkingFee(parkingMin))