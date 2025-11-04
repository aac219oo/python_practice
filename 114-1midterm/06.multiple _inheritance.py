'''
題目 6：多重繼承的應用
設計一個 `SmartDevice` 同時繼承 `Switchable` 與 `Adjustable`，實作冷氣與桌燈的操作行為。
'''
class Switchable:
    def turn_on(self):
        return f"{self.name}已開啟"
    def turn_off(self):
        return f"{self.name}已關閉"


class Adjustable:

    def set_level(self):
        return f"調整{self.level}"


class SmartDevice(Switchable, Adjustable):

    def __init__(self, name, status, level) -> None:
        self.name = name
        self.status = status
        self.level = level
        super().__init__()


smartDevices = [SmartDevice("冷氣", True, 4), SmartDevice("桌燈", False, 0)]
for smartDevice in smartDevices:
    if smartDevice.status:
        print(f"{smartDevice.turn_on()}，{smartDevice.set_level()}")
    else:
        print(f"{smartDevice.turn_off()}，{smartDevice.set_level()}")
