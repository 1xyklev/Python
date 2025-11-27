from tkinter import *
import random
import time

class Ball:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
        self.canvas.move(self.id, 245, 100)

    def draw(self):
        self.canvas.move(self.id, 0, -1)    # 매 프레임 공이 위로 1픽셀씩

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