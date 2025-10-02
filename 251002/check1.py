from tkinter import*
from tkinter.messagebox import showinfo
root = Tk()
root.geometry("300x200")
root.title("Ceckbox Demo")

agree = StringVar()     # 체크박스의 상태를 저장하는 변수

agree.set("비동의")     # 초기 상태를 "비동의"로 설정

def event_proc():   # 체크박스 클릭 시 실행될 함수
    showinfo(title="결과", message=agree.get())

Checkbutton(root,   # 체크박스 생성 및 배치
            text = "동의합니다.",
            command=event_proc,
            variable=agree,
            onvalue="동의",
            offvalue="비동의").pack()

root.mainloop()