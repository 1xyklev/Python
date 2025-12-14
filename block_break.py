import pygame
import random

# 초기화
pygame.init()
size = [600, 400]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("블록 깨기")
clock = pygame.time.Clock()
# 실행 상태(running, game_over) 초깃값
running, game_over, score = True, False, 0 

font = pygame.font.SysFont(None, 25) 

pw, ph, ps = 80, 10, 6
bs = 10
bw, bh = 50, 20
rows, cols = 3, 10

# 초기화 함수
def reset_ball():
    global ball, ball_dx, ball_dy
    # Rect 객체: 공의 위치, 크기, 충돌 영역 정의
    ball = pygame.Rect(size[0] // 2 - bs // 2, size[1] // 2 - bs // 2, bs, bs)
    ball_dx = random.choice([-3, 3]) 
    ball_dy = -3 

def reset_paddle():
    global paddle
    paddle = pygame.Rect(size[0] // 2 - pw // 2, size[1] - ph - 10, pw, ph)

def setup_blocks():
    global blocks
    blocks = []
    # 블록 생성: Rect 객체 이용 -> 규칙적으로 블록 배치
    for r in range(rows):
        for c in range(cols):
            x = c * (bw + 5) + 30
            y = r * (bh + 5) + 30
            blocks.append(pygame.Rect(x, y, bw, bh))

reset_paddle(); reset_ball(); setup_blocks() # 초기 실행


# 게임 오버1
def show_game_over_screen(message):
    screen.fill((0, 0, 0))
    tc = (255, 0, 0) if message == "GAME OVER" else (255, 255, 255)
    title = font.render(message, True, tc)
    score_t = font.render(f"SCORE: {score}", True, (255, 255, 255)) 
    restart_t = font.render("Press ENTER to restart", True, (255, 255, 255))
    
    # 텍스트 배치, 그리기
    cx, cy = size[0] // 2, size[1] // 2
    screen.blit(title, title.get_rect(center=(cx, cy - 30))) 
    screen.blit(score_t, score_t.get_rect(center=(cx, cy + 20)))
    screen.blit(restart_t, restart_t.get_rect(center=(cx, cy + 70)))
    
    pygame.display.flip() 
    
    # 입력 대기: 게임이 멈춘 상태에서 ENTER/ESC 입력 기다림
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: pygame.quit(); return False 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN: return True 
                if event.key == pygame.K_ESCAPE: pygame.quit(); return False
        clock.tick(10) 

def restart_game():
    global game_over, score
    game_over, score = False, 0
    reset_paddle(); reset_ball(); setup_blocks()


# 루프
# 게임의 모든 계산(3.2, 3.3), 출력(3.4) 60FPS로 반복
while running:
    # 이벤트
    for event in pygame.event.get():
        if event.type == pygame.QUIT: running = False

    if not game_over:
        # 3.2 움직임
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and paddle.left > 0: paddle.x -= ps
        if keys[pygame.K_RIGHT] and paddle.right < size[0]: paddle.x += ps
        
        ball.x += ball_dx; ball.y += ball_dy

        # 3.3 충돌 처리
        if ball.left <= 0 or ball.right >= size[0]: ball_dx *= -1 # 좌우 벽
        if ball.top <= 0: ball_dy *= -1 # 상단 벽
        
        # 패들 충돌: colliderect로 겹침 확인 -> 공의 y 방향 반전
        if ball.colliderect(paddle) and ball_dy > 0: ball_dy *= -1 
        
        # 패배 조건: 공의 바닥 좌표가 화면 높이(size[1])를 넘으면 Game Over
        if ball.bottom >= size[1]: game_over = True 

        # 블록 충돌: collidelist로 블록 충돌 확인 -> 제거
        hit_index = ball.collidelist(blocks)
        if hit_index != -1:
            blocks.pop(hit_index); score += 10; ball_dy *= -1 

        if not blocks: game_over = True # 승리
            
    screen.fill((0, 0, 0))

    for block in blocks:
        pygame.draw.rect(screen, (0, 255, 0), block) 
    pygame.draw.rect(screen, (0, 0, 255), paddle)
    pygame.draw.circle(screen, (255, 0, 0), ball.center, bs // 2)

    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    # 게임 오버2
    if game_over:
        message = "Game Cleared!" if not blocks else "GAME OVER"
        should_restart = show_game_over_screen(message)
        if should_restart: restart_game()
        elif should_restart == False: running = False
    
    pygame.display.flip()
    # 프레임 제한: 루프 속도를 초당 60회 제한 (60 FPS)
    clock.tick(60) 

pygame.quit()