'''
images\113-2midterm\parkingFee.jpg
第8题
停車場收費採取分段收費，方式如下。請寫一程式能計算出停車費。
>> 超過15分鐘則算滿半小時。
>> 2小時以內，每半小時20元。
>> 超過2小時，未滿4小時，每半小時$30元。
>> 超過4小時，未滿6小時，每半小時$40元。
>> 滿6小時以上，直接以全日上限$500計價

例如:停車74分鐘，收費$40元
     停車75分鐘，收費$60元
     停車119分鐘，收費$80元
     停車120分鐘，收費$120元
     停車250分鐘，收費$320元
'''
inTwoHour = 20
overTwoHour = 30
overFourHour = 40
overSixHour = 500

inputParkingTime = int(input("請輸入總停車時間(分鐘)："))

def parkingFee(min):
     calParkingTime = min // 30
     if min % 30 >= 15:
          calParkingTime += 1

     if 30 > min > 0:
          fee = inTwoHour           
     elif 120 > min >= 30:
          fee = inTwoHour * calParkingTime
     elif 240 > min >= 120:
          fee = overTwoHour * calParkingTime
     elif 360 > min >= 240:
          fee = overFourHour * calParkingTime
     elif min >= 360:
          fee = overSixHour
     else:
          fee = "請輸入正確時間"
     return fee

print(parkingFee(inputParkingTime))