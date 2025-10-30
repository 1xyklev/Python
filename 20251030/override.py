class Animal:
    def __init__(self, name=""):
        self.name = name

    def eat(self):
        print("동물이 먹고 있습니다.")

class Dog(Animal):
    def __init__(self):
        super().__init__()

    def eat(self):
        super().eat()   # 부모 클래스의 메소드가 호출된다.
        print("강아지가 먹고 있습니다.")

d = Dog()
d.eat()