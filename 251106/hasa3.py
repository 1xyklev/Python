class Vehicle:
    def drive(self):
        print("차량이 이동 중입니다.")

class Car:
    def __init__(self):
        self.vehicle = Vehicle()    # Car는 Vehicle을 가진다

    def drvie(self):
        self.vehicle.drive()    # Vehicle의 기능 사용
        print("자동차가 도로를 달립니다.")

car = Car()
car.drive()