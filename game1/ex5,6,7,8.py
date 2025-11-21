#Bouncing Ball Game(패들추가)
from tkinter import *
import random
import time

tk = Tk()
tk.title("Game")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1) 

canvas = Canvas(tk, width=500, height=400, bd=0, highlightthickness=0)
canvas.pack()
tk.update()

class Ball:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color) #도형 ID
        self.canvas.move(self.id, 245, 100) #canvas.move(객체ID, X방향이동, Y방향이동)

        starts = [-3, -2, -1, 1, 2, 3]
        random.shuffle(starts)       # 리스트 순서를 섞기
        self.x = starts[0]          # 섞인 리스트의 첫 번째 값을 사용

        self.y = -3 # y 방향은 위로 -3 속도로 시작

        self.canvas_height = self.canvas.winfo_height() # 캔버스 높이 저장
        self.canvas_width = self.canvas.winfo_width()

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

class Paddle: #패들 클래스 추가
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 100, 10, fill=color)
        self.canvas.move(self.id, 200, 300)

        self.x = 0
        self.canvas_width = self.canvas.winfo_width()
        
        self.canvas.bind_all('<KeyPress-Left>', self.turn_left) # 키보드 이벤트 연결
        self.canvas.bind_all('<KeyPress-Right>', self.turn_right)

    def turn_left(self, evt):
        self.x = -2   # 왼쪽으로 이동 속도

    def turn_right(self, evt):
        self.x = 2    # 오른쪽으로 이동 속도

    def draw(self): # 패들을 x 방향으로만 이동
        self.canvas.move(self.id, self.x, 0)
        pos = self.canvas.coords(self.id)

        # 화면 왼쪽/오른쪽 끝을 넘지 않게 막기
        if pos[0] <= 0:
            self.x = 0
        elif pos[2] >= self.canvas_width:
            self.x = 0

ball = Ball(canvas, 'red')
paddle = Paddle(canvas, 'blue') #추가

while True:
    ball.draw()
    paddle.draw() #추가
    tk.update_idletasks() 
    tk.update() 
    time.sleep(0.01)

tk.mainloop()