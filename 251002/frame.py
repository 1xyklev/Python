from tkinter import*

root = Tk()      # 부모 위젯 생성
root.geometry("300x200")

frame = Frame(root, width=200, height = 100)     # Frame 위젯 생성
frame.pack()    # Frame 위젯 배치

button1 = Button(frame, text="버튼 1")  # 버튼 1
button1.pack(side="left")

button2 = Button(frame, text="버튼 2")  # 버튼 2
button2.pack(side="left")

root.mainloop()     # 이벤트 루프 시작