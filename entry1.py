from tkinter import*

def get_entry_value():
    value = entry.get()
    print("입력된 값:", value)

root = Tk()     # 부모 위젯 생성
root.geometry("300x200")

entry = Entry(root)      # 엔트리 위젯 생성
entry.pack()    # 엔트리 위젯 배치

button = Button(root, text = "확인", command = get_entry_value)     # 버튼 위젯 생성
button.pack()   # 버튼 위젯 배치

root.mainloop()     # 이벤트 루프 시작