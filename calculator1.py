from tkinter import*
from math import*

# eval() 함수를 호출하여서 사용자가 입력한 수식을 계산한다. 레이블의 configure()를 호출하여 레이블의 텍스트를 변경한다.
def calculate(event):
    label.configure(text="결과: " + str(eval(entry.get())))

root = Tk()

Label(root, text = "파이썬 수식 입력: ").pack()

entry = Entry(root)

# 엔트리 위젯에서 엔터키를 치면 calculate()가 호출되게 연결한다. 이벤트 처리 부분을 참고한다.
entry.bind("<Return>", calculate)
entry.pack()

label = Label(root, text = "결과:")
label.pack()

root.mainloop()