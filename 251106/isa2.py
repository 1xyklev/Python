class Person:
    def speak(self):
        print("사람이 말을 합니다.")

class Student(Person):
    def study(self):
        print("학생이 공부합니다.")


stu = Student()
stu.speak()
stu.study()