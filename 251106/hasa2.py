class Person:
    def speak(self):
        print("사람이 말을 합니다.")

class Student:
    def __init__(self):
        self.person = Person()  # Student는 Person을 가진다

    def study(self):
        self.person.speak()     # 포함된 Person의 행동 사용
        print("학생이 공부합니다.")

stu = Student()
stu.study()