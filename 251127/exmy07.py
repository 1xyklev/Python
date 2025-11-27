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
        self.canvas.move(self.id, 245, 100)

        # 공의 속도, 좌우로 움직이던 것을 *수정
        starts = [-3, -2, -1, 1, 2, 3]
        random.shuffle(starts)  # 리스트 순서를 섞기
        self.x = starts[0]  # 랜덤한 좌우 속도 선택


        self.y = -3     # y 방향은 위로 -3 속도로 시작

        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()   # 수정

    def draw(self):     # 수정
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        # print(self.canvas.coords(self.id))

        if pos[1] <= 0:     # 공의 윗부분이 캔버스 위쪽에 닿으면 -> 아래로 이동
            self.y = 1
        
        if pos[3] >= self.canvas_height:    # 공의 아랫부분이 캔버스 아래쪽에 닿으면 → 위로 이동
            self.y = -1

        # 좌우 벽 충돌 시 방향 반전
        if pos[0] <= 0:     # 왼쪽 벽에 닿으면 -> 오른쪽으로 튕김
            self.x = 3
        
        if pos[2] >= self.canvas_width:     # 오른쪽 벽에 닿으면 -> 왼쪽으로 튕김
            self.x = -3

ball = Ball(canvas, 'red')

while True:
    ball.draw()
    tk.update_idletasks() #tkinter내부 작업 처리
    tk.update() 
    time.sleep(0.01)

tk.mainloop()

# pos[0] -> 공의 왼쪽 x 좌표
# pos[1] -> 공의 위쪽 y 좌표
# pos[2] -> 공의 오른쪽 x 좌표
# pos[3] -> 공의 아래쪽 y 좌표