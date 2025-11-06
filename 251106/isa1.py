class Animal:
    def move(self):
        print("동물이 움직입니다.")

class Dog(Animal):
    def move(self):
        super().move()  # 부모 클래스(Animal)의 move() 호출
        print("개가 달립니다.")

dog = Dog()
dog.move()