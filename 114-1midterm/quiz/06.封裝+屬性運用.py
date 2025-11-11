class Parking:
    def __init__(self, car_number) -> None:
        self.car_number = car_number
        self.__minutes = 0

    def parking_time(self, min):
        self.__minutes = min

    def calParkingFee(self):
        perHourFee = 30
        perDaylimitFee = 300
        calHour = self.__minutes // 60
        if self.__minutes % 60 >= 30:
            calHour += 1
        totalFee = perHourFee * calHour
        if totalFee >= 300:
            totalFee = perDaylimitFee
        elif 1 <= self.__minutes <= 60:
            totalFee = perHourFee

        return print(f"車號{self.car_number}的停車費為{totalFee}元") 
    
parking_price = Parking("ABC123")
parking_price.parking_time(200)
parking_price.calParkingFee()