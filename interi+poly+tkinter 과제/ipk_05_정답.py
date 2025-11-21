from tkinter import *

class Pet:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "..."

class Dog(Pet):
    def speak(self):
        return "멍멍!"

class Cat(Pet):
    def speak(self):
        return "야옹!"

class Person:
    def __init__(self, name, pet=None):
        self.name = name
        self.pet = pet

root = Tk()
root.title("문제5")
root.geometry("700x300")

person = Person("홍길동")

label1 = Label(root, text=" 반려동물 등록하기")
label1.pack(pady=8)

frame = Frame(root)
frame.pack(pady=10)

# 반려동물 이름
label2 = Label(frame, text="반려동물 이름: ")
label2.grid(row=0, column=0, padx=5, pady=5)
entry = Entry(frame)
entry.grid(row=0, column=1, columnspan=3, padx=5, pady=5, sticky="w")

# 종류
label3 = Label(frame, text="종류: ")
label3.grid(row=1, column=0, padx=5, pady=5)
pet_type = StringVar(value="Dog")
Radiobutton(frame, text="강아지", value="Dog", variable=pet_type).grid(row=1, column=1, padx=5, sticky="w")
Radiobutton(frame, text="고양이", value="Cat", variable=pet_type).grid(row=1, column=2, padx=5, sticky="w")

# 옵션
label4 = Label(frame, text="옵션:", width=15, anchor="e")
label4.grid(row=2, column=0, padx=5, pady=5)
vaccinated = IntVar(value=0)
neutered = IntVar(value=0)
Checkbutton(frame, text="예방접종 완료", variable=vaccinated).grid(row=2, column=1, padx=5, sticky="w")
Checkbutton(frame, text="중성화 완료", variable=neutered).grid(row=2, column=2, padx=5, sticky="w")

# 결과 출력
result_var = StringVar(value="등록 정보를 확인하세요.")
label5 = Label(frame, textvariable=result_var, fg="blue", wraplength=500, justify="left")
label5.grid(row=3, column=0, columnspan=4, pady=15)

def register():
    pet_name = entry.get() or "이름없음"
    kind = pet_type.get()
    pet = Dog(pet_name) if kind == "Dog" else Cat(pet_name)
    person.pet = pet

    vac = "O" if vaccinated.get() else "X"
    neu = "O" if neutered.get() else "X"
    kind_kor = "강아지" if kind == "Dog" else "고양이"

    msg = (f"{person.name}의 반려동물 등록 완료!\n"
           f"이름: {pet.name} ({kind_kor})\n"
           f"소리: {pet.speak()}\n"
           f"예방접종: {vac}, 중성화: {neu}")
    result_var.set(msg)

def reset():
    entry.delete(0, END)
    pet_type.set("Dog")
    vaccinated.set(0)
    neutered.set(0)
    person.pet = None
    result_var.set("등록 정보를 확인하세요.")

frm_btn = Frame(root)
frm_btn.pack(pady=5)
Button(frm_btn, text="등록하기", width=12, command=register).pack(side="left", padx=15)
Button(frm_btn, text="초기화", width=12, command=reset).pack(side="left", padx=15)

root.mainloop()