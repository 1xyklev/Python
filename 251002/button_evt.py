from tkinter import*

def callback():
    """
    콜백 함수: 버튼이 클릭되면 호출되어 버튼의 텍스트를 변경한다.
    """
    button["text"] = "버튼이 클릭되었음!"

# Tkinter 윈도우 생성
root = Tk()

# 버튼 생성 및 콜백 함수와 연결
button = Button(root, text="클릭", command=callback)
button.pack(side=LEFT)  # 버튼을 윈도우에 팩 배치

root.mainloop()     # Tkinter 이벤트 루프 실행