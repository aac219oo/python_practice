class RockClimbing:

    def __init__(self, location, type) -> None:
        self.location = location
        self.type = type

    def show(self):
        print("在" + self.location)
        print("正在" + self.type)


class outside(RockClimbing):

    def __init__(self, location, type, inAndOut, multiPitch, gear) -> None:
        self.location = location
        self.type = type
        self.gear = gear
        self.inAndOut = inAndOut
        self.multiPitch = multiPitch
    def environment(self):
        print(self.inAndOut)
        print(self.multiPitch + "多繩距")
        print(self.gear + "要帶")


class inside(RockClimbing):

    def __init__(self, location, type, gear, inAndOut) -> None:
        self.location = location
        self.type = type
        self.gear = gear
        self.inAndOut = inAndOut
    def environment(self):
        print(self.inAndOut)
        print(self.gear + "要帶")


climb1 = outside("龍洞", "傳統攀登", "室外", "有", "岩楔")
climb2 = inside("大埔岩館", "運動攀登", "Grigri", "室內")
climb1.show()
climb1.environment()
climb2.show()
climb2.environment()

