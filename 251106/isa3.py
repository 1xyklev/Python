class Vehicle:
    def drive(self):
        print("차량이 이동 중입니다.")

class Car(Vehicle):
    def drive(self):
        super().drive()     # 부모 클래스(Vehicle)의 drive() 호출
        print("자동차가도로를 달립니다.")

car = Car()
car.drive()