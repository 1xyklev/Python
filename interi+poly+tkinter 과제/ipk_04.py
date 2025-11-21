from tkinter import *

class Person:
    def __init__(self, name: str):  # :str은 타입 힌트
        self.name = name

class Student(Person):
    def __init__(self, name: str):
        super().__init__(name)
        self.classes = []

    def enrollCourse(self, subject: str):
        if subject not in self.classes:
            self.classes.append(subject)

    def clearCourses(self):
        self.classes.clear()

root = Tk()
root.title("문제4")
root.geometry("380x280")

stu = Student("홍길동")

lb1 = Label(root, text=f"학생: {stu.name}").pack(pady=8)

frame = Frame(root)
frame.pack(pady=10, anchor="center")

var_py = IntVar(value=0)
var_ai = IntVar(value=0)
var_ds = IntVar(value=0)

Checkbutton(frame, text="Python", variable=var_py).grid(row=0, column=0, padx=8, pady=4)
Checkbutton(frame, text="AI", variable=var_ai).grid(row=0, column=1, padx=8, pady=4)
Checkbutton(frame, text="DataScience", variable=var_ds).grid(row=0, column=2, padx=8, pady=4)

result = StringVar(value="과목을 선택하고 [등록하기]를 누르세요.")
lb2 = Label(root, textvariable=result, wraplength=340, justify="left").pack(pady=10)

def register_courses():
    stu.clearCourses()
    if var_py.get(): stu.enrollCourse("Python")
    if var_ai.get(): stu.enrollCourse("AI")
    if var_ds.get(): stu.enrollCourse("DataScience")

    if stu.classes:
        result.set(f"등록된 과목: {', '.join(stu.classes)}")
    else:
        result.set("선택된 과목이 없습니다.")

def reset_all():
    var_py.set(0)
    var_ai.set(0)
    var_ds.set(0)
    stu.clearCourses()
    result.set("모든 선택을 해제했습니다.")

btn_frame = Frame(root)
btn_frame.pack(pady=6)

Button(btn_frame, text="등록하기", command=register_courses).pack(side="left", padx=8)
Button(btn_frame, text="초기화", command=reset_all).pack(side="left", padx=8)

root.mainloop()