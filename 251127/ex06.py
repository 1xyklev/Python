from tkinter import *
import random
import time

class Ball:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color) #도형 ID
        self.canvas.move(self.id, 245, 100) #canvas.move(객체ID, X방향이동, Y방향이동)

        # 공의 속도(방향)
        self.x = 0        # 좌우 속도 (0은 좌우로 안움직임)
        self.y = -1       # 위쪽(-1)으로 이동

        # 캔버스 높이 저장
        self.canvas_height = self.canvas.winfo_height()

    def draw(self): #수정
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)      # 현재 공의 위치 가져오기 [x1, y1, x2, y2]
        #print(self.canvas.coords(self.id))

        if pos[1] <= 0: # 천장에 닿음 → 아래로 방향 전환
            self.y = 1

        if pos[3] >= self.canvas_height:
            self.y = -1

#Tkinter
tk = Tk()
tk.title("Game")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1) #게임창이 항상 위로 있도록

canvas = Canvas(tk, width=500, height=400, bd=0, highlightthickness=0)
canvas.pack()
tk.update()

ball = Ball(canvas, 'red')

while True:
    ball.draw()
    tk.update_idletasks() #tkinter내부 작업 처리
    tk.update() 
    time.sleep(0.01)

tk.mainloop()