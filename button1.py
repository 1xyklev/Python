from tkinter import*

def button_clicked():
    print("버튼이 클릭되었습니다!")

root = Tk()     # 부모 위젯 생성
root.geometry("300x200")

button = Button(root, text = "클릭하세요", command = button_clicked)    # 버튼 위젯 생성
button.pack()   # 버튼 위젯 배치

root.mainloop()     # 이벤트 루프 시작