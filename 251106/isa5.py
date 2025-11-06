class Bird:
    def fly(self):
        print("새가 날아갑니다.")

class Penguin(Bird):
    def fly(self):
        super().fly()   # 부모 클래스(Bird)의 fly() 호출
        print("펭귄은 날지 못하지만 수영을 합니다.")

p = Penguin()
p.fly()