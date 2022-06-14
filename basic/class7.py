# 클래스 상속
# class 상속받을 클래스명(상속할 클래스)


# class Parent:
#     def __init__(self) -> None:
#         self.value = "테스트"
#         print("Parent 클래스의 __init__ 호출")

#     def test(self):
#         print("Parent 클래스의 test 호출")


# class Child(Parent):
#     def __init__(self) -> None:
#         # 부모의 init 호출 => 부모 객체 생성될 수 있도록 명시해줘야 함(안해주면 멤버변수 접근에 제한됨)
#         Parent.__init__(self)
#         print("Child 클래스의 __init__ 호출")

# child = Child()
# child.test()
# print(child.value)


# class Car:

#     speed = 0

#     def up_speed(self, value):
#         self.speed = self.speed + value

#     def down_speed(self, value):
#         self.speed = self.speed - value


# class Sedan(Car):

#     seatNum = 0

#     def getSeatNum(self):
#         return self.seatNum


# class Truck(Car):

#     capacity = 0

#     def getCapacity(self):
#         return self.capacity


# sedan1, truck1 = Sedan(), Truck()


# sedan1.up_speed(100)
# truck1.up_speed(80)

# sedan1.seatNum = 5
# truck1.capacity = 50

# print("승용차의 속도는 {}km, 좌석수는 {}개".format(sedan1.speed, sedan1.getSeatNum()))
# print("트럭의 속도는 {}km, 총 중량은 {}톤".format(truck1.speed, truck1.getCapacity()))


class AudioVisual:
    def __init__(self, power, volume) -> None:
        self.power = power
        self.volume = volume

    def switch(self, on_off):
        self.power = on_off

    def set_volume(self, volume):
        self.volume = volume


class Audio(AudioVisual):
    def __init__(self, power, volume):
        super().__init__(power, volume)

    def tune(self):
        msg = "La La La..." if self.power else "turn it on"
        print(msg)


class TV(AudioVisual):
    def __init__(self, power, volume, size):
        super().__init__(power, volume)
        self.size = size

    def watch(self):
        msg = "have fun!!!" if self.power else "switch on"
        print(msg)


tv1 = TV(False, 12, 55)
tv1.switch(True)
tv1.watch()

audio1 = Audio(True, 15)
audio1.set_volume(6)
audio1.tune()