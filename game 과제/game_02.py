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

# 점수 변수
score = 0
score_text = canvas.create_text(450, 20, text="Score: 0", font=("Arial", 14), fill="black")


# 재시작
def restart_game():
    global score
    restart_btn.destroy()
    canvas.delete("all")

    # 점수 초기화
    score = 0
    canvas.create_text(450, 20, text=f"Score: {score}", font=("Arial", 14), fill="black", tag="score")

    start_game()


def start_game():
    global ball, paddle, game_over_text, restart_btn, score_text

    canvas.delete("all")

    # 점수 표시 다시 생성
    score_text = canvas.create_text(450, 20, text="Score: 0", font=("Arial", 14), fill="black")

    game_over_text = None
    restart_btn = None

    # Paddle 생성
    paddle = Paddle(canvas, 'blue')

    # Ball 생성 (paddle 전달)
    ball = Ball(canvas, 'red', paddle)

    # 게임 루프
    while True:
        if not ball.hit_bottom:
            ball.draw()
            paddle.draw()
        else:
            if game_over_text is None:
                game_over()
            break

        tk.update_idletasks()
        tk.update()
        time.sleep(0.01)


# GAME OVER 화면
def game_over():
    global game_over_text, restart_btn

    game_over_text = canvas.create_text(
        250, 150,
        text="GAME OVER",
        font=("Arial", 30, "bold"),
        fill="red"
    )

    # 재시작 버튼 생성 + 배치
    restart_btn = Button(tk, text="Restart", font=("Arial", 14), command=restart_game)
    restart_btn.place(x=210, y=200)


class Ball:
    def __init__(self, canvas, color, paddle):
        self.canvas = canvas
        self.paddle = paddle
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
        self.canvas.move(self.id, 245, 100)

        starts = [-3, -2, -1, 1, 2, 3]
        random.shuffle(starts)
        self.x = starts[0]
        self.y = -3

        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()

        self.hit_bottom = False

    def hit_paddle(self, pos):
        paddle_pos = self.canvas.coords(self.paddle.id)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                return True
        return False

    def draw(self):
        global score

        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)

        if pos[1] <= 0:
            self.y = 3
        if pos[3] >= self.canvas_height:
            self.hit_bottom = True

        # Paddle 충돌
        if not self.hit_bottom and self.hit_paddle(pos):
            self.y = -3
            score += 1
            canvas.itemconfig(score_text, text=f"Score: {score}")

        if pos[0] <= 0:
            self.x = 3
        if pos[2] >= self.canvas_width:
            self.x = -3


class Paddle:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 100, 10, fill=color)
        self.canvas.move(self.id, 200, 300)

        self.x = 0
        self.canvas_width = self.canvas.winfo_width()

        self.canvas.bind_all('<KeyPress-Left>', self.turn_left)
        self.canvas.bind_all('<KeyPress-Right>', self.turn_right)

    def turn_left(self, evt):
        self.x = -2

    def turn_right(self, evt):
        self.x = 2

    def draw(self):
        self.canvas.move(self.id, self.x, 0)
        pos = self.canvas.coords(self.id)

        if pos[0] <= 0:
            self.x = 0
        elif pos[2] >= self.canvas_width:
            self.x = 0


# 게임 시작
start_game()
tk.mainloop()