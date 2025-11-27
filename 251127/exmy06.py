from tkinter import *
import random
import time

class Ball:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color) #도형 ID
        self.canvas.move(self.id, 245, 100)

        # 공의 속도를 나타내는 변수
        self.x = 0  # 좌우 속도 (0은 좌우로 안움직임)
        self.y = -1     # 위쪽으로 이동

        # 캔버스의 높이를 가져와서 저장
        self.canvas_height = self.canvas.winfo_height()

    def draw(self):
        self.canvas.move(self.id, self.x, self.y)   # 공을 (x,y)만큼 이동
        pos = self.canvas.coords(self.id)   # 현재 공의 위치
        # print(self.canvas.coords(self.id))

        if pos[1] <= 0:     # pos[1]은 공의 윗부분 y좌표
            self.y = 1     # 계속 위로만 움직임
        
        if pos[3] >= self.canvas_height:    # pos[3]은 공의 아랫부분 y좌표
            self.y = -1     # 공이 아래쪽에 닿아도 다시 위로 올라가도록 강제

tk = Tk()
tk.title("Game")
tk.resizable(0,0)   # 창 크기 조절 불가능
tk.wm_attributes("-topmost", 1)     # 게임창이 항사 위로 있도록

canvas = Canvas(tk, width = 500, height = 400, bd = 0, highlightthickness = 0)  # bd = 0, hightlightthickness = 0 은 테두리 제거
canvas.pack()
tk.update()

ball = Ball(canvas, 'red')

while True:
    ball.draw()
    tk.update_idletasks()   # tkinter 내부 작업 처리
    tk.update()
    time.sleep(0.01)    # 0.01초 딜레이

tk.mainloop()