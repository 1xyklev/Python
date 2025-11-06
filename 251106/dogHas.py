class Animal:
    def speak(self):
        print("동물이 소리를 냅니다.")

class Dog:
    def __init__(self):
        self.animal = Animal()  # Dog has an Animal

    def speak(self):
        # Animal의 기능을 사용하면서 추가 행동을 할 수도 있음
        self.animal.speak()
        print("멍멍!")

dog = Dog()
dog.speak()