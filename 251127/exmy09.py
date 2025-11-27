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
        self.paddle = paddle    # 패들 객체 기억하도록 수정
        self.canvas.move(self.id, 245, 100)

        starts = [-3, -2, -1, 1, 2, 3]
        random.shuffle(starts)
        self.x = starts[0]  

        self.y = -3 

        self.canvas_height = self.canvas.winfo_height() 
        self.canvas_width = self.canvas.winfo_width()

    # 추가: 공이 패들에 부딪혔는지 검사하는 함수
    def hit_paddle(self, pos):
        paddle_pos = self.canvas.coords(self.paddle.id)     # 패들의 위치 [px1, py1, px2, py2]

        # 가로 방향으로 공과 패들이 겹치는지 확인
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                return True
        return False
    
    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id) 
        print(self.canvas.coords(self.id))

        if pos[1] <= 0:     # 위쪽 벽에 닿으면 아래로 이동
            self.y = 3  # 속도 수정
        if pos[3] >= self.canvas_height:    # 아래쪽(바닥)에 닿으면 위로 튕김
            self.y = -3     # 속도 수정    

        # 추가: 패들과 부딪혔는지 검사
        if self.hit_paddle(pos) == True:    # True면 공이 패들과 부딪힘
            self.y = -3     # 위로 튕기게 함

        if pos[0] <= 0: # 왼쪽 벽에 닿으면 → 오른쪽으로 튕김
            self.x = 3
        if pos[2] >= self.canvas_width: # 오른쪽 벽에 닿으면 → 왼쪽으로 튕김
            self.x = -3

class Paddle:   # 패들 클래스 추가
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 100, 10, fill = color)
        self.canvas.move(self.id, 200, 300)

        self.x = 0  # 패들의 이동 속도/ 처음에는 움직이지 않음
        self.canvas_width = self.canvas.winfo_width()   # 너비를 저장하고 있기(벽에 부딪히면 처리하기 위해서)

        self.canvas.bind_all('<KeyPress-Left>', self.turn_left)     # 키보드의 왼쪽 화살표 키를 누르면 turn_left() 실행
        self.canvas.bind_all('<KeyPress-Right>',self.turn_right)    # 키보드의 오른쪽 화살표 키를 누르면 turn_right() 실행

    def turn_left(self, evt):
        self.x = -2     # 매 프레임마다 왼쪽으로 2px 이동

    def turn_right(self, evt):
        self.x = 2  # 매 프레임마다 오른쪽으로 2px 이동

    def draw(self):     # 패들을 x축 방향으로만 이동
        self.canvas.move(self.id, self.x, 0)
        pos = self.canvas.coords(self.id)

        # 화면 왼쪽/오른쪽 끝을 넘지 않게 막기
        if pos[0] <= 0:     # pos[0] -> 패들의 왼쪽 끝 좌표
            self.x = 0  # 0보다 작거나 같으면 이동 멈춤
        elif pos[2] >= self.canvas_width:   # pos[2] -> 패들의 오른쪽 끝 좌표
            self.x = 0  # 캔버스 너비보다 크거나 같으면 이동 멈춤

paddle = Paddle(canvas, 'blue') # 수정 - 패들 먼저 생성해야함
ball = Ball(canvas, 'red')

while True:
    ball.draw()
    paddle.draw() # 패들 draw 추가
    tk.update_idletasks() 
    tk.update() 
    time.sleep(0.01)

tk.mainloop()

# pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]
# → 공의 오른쪽 끝이 패들의 왼쪽보다 오른쪽에 있고, 
# → 공의 왼쪽 끝이 패들의 오른쪽보다 왼쪽에 있으면 가로 방향으로 겹침.

# pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]
# → 공의 아래쪽 끝이 패들의 위쪽과 아래쪽 사이에 있으면 세로 방향으로 겹침.