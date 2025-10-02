from tkinter  import*
from random import randint

def place_random_buttons():
    """
    임의의 위치와 크기로 버튼을 배치하는 함수
    """
    for button in buttons:
        x = randint(50, 400)
        y = randint(50, 250)
        width = randint(50, 100)
        height = randint(20, 50)
        button.place(x=x, y=y, width=width, height=height)

# Tkinter 위도우 생성
root = Tk()
root.geometry("500x300")    # 윈도우 크기 설정

buttons = []    # 버튼을 담을 리스트
colors = ["red", "green", "blue", "yellow"]

# 버튼 생성 및 리스트에 추가
for color in colors:
    button = Button(root, text = color, bg = color, fg = "white")
    buttons.append(button)

place_random_buttons()  # 초기 버튼 배치

# 새로고침 버튼 생성 및 배치
refresh_button = Button(root, text="새로고침", command=place_random_buttons)
refresh_button.place(x=150, y=250)

root.mainloop()     # Tkinter 이벤트 루프 실행