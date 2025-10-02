from tkinter import *

def print_fields():
    # 아이디와 패스워드 입력값을 가져가서 출력합니다.
    print("아이디: %s/n패스워드: %s"%(e1.get(), e2.get()))

root = Tk()     # Tkinter 윈도우 생성
Label(root, text = "아이디").grid(row=0)    # 아이디와 패스워드 라벨 생성 및 배치
Label(root, text = "패스워드").grid(row=1)

# 아이디와 패스워드 입력 위젯 생성 및 배치
e1 = Entry(root)
e2 = Entry(root)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

# 로그인 및 취소 버튼 생성 및 배치
Button(root, text='로그인', command=print_fields).grid(row=3, column=0, sticky=W, pady=4)
Button(root, text='취소', command=root.quit).grid(row=3, column=1, sticky=W, pady=4)

# 윈도우 루프 시작
root.mainloop()