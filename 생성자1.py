class Car:
    speed=0
    def upSpeed(self, value):
        self.speed+=value

        print("현재속도: %d" %self.speed)

class Sedan(Car):
    def upSpeed(self, value):
        self.speed+=value

        if self.speed>150:
            self.speed=150
            print("현재속도: %d" %self.speed)

class Truck(Car):
    pass

sedan1, truck1=None, None

truck1=Truck()
sedan1=Sedan()

truck1.upSpeed(200)
sedan1.upSpeed(200)
