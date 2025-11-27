from tkinter import *
import random
import time

tk = Tk()
tk.title("Game")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1) #게임창이 항상 위로 있도록

canvas = Canvas(tk, width=500, height=400, bd=0, highlightthickness=0)
canvas.pack()
tk.update()

class Ball:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color) #도형 ID
        self.canvas.move(self.id, 245, 100) #canvas.move(객체ID, X방향이동, Y방향이동)

        # 공의 속도, 좌우로 움직이던 것을 *수정
        starts = [-3, -2, -1, 1, 2, 3]
        random.shuffle(starts)       # 리스트 순서를 섞기
        self.x = starts[0]          # 섞인 리스트의 첫 번째 값을 사용

        self.y = -3 # y 방향은 위로 -3 속도로 시작

        # 캔버스 높이 저장
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width() #수정

    def draw(self): #수정
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)      # 현재 공의 위치 가져오기 [x1, y1, x2, y2]
        #print(self.canvas.coords(self.id))

        if pos[1] <= 0:
            self.y = 1

        if pos[3] >= self.canvas_height:
            self.y = -1
                  
        if pos[0] <= 0: # 왼쪽 벽에 닿으면 → 오른쪽으로 튕김
            self.x = 3

        if pos[2] >= self.canvas_width: # 오른쪽 벽에 닿으면 → 왼쪽으로 튕김
            self.x = -3

ball = Ball(canvas, 'red')

while True:
    ball.draw()
    tk.update_idletasks() #tkinter내부 작업 처리
    tk.update() 
    time.sleep(0.01)

tk.mainloop()