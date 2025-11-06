class Animal:
    def move(self):
        print("도움ㄹ이 움직입니다.")

class Dog:
    def __init__(self):
        self.animal = Animal()  # 포함 관계 (Dog는 Animal을 가진다)

    def move(self):
        self.animal.move()  # Animal의 행동 사용
        print("개가 달립니다.")

dog = Dog()
dog.move()