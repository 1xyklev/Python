#7. 그리기(Drawing)
import pygame

pygame.init()

WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Step 7 - Drawing 추가")


#사용자 이미지 로드 
img = pygame.image.load("dukbird.png")   # ← 여기에 파일 이름 입력! (png, jpg 등)
img = pygame.transform.scale(img, (50, 50))  # ← 크기 조절 (원하면)
rect = img.get_rect()
rect.center = (WIDTH // 2, HEIGHT // 2)

speed = 2
running = True

while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    if event.type == pygame.KEYDOWN:
      print("KEYDOWN:", event.key)
    if event.type == pygame.KEYUP:
      print("KEYUP:", event.key)
    if event.type == pygame.MOUSEBUTTONDOWN:
      print("Mouse Click:", event.pos)

  # 실시간 키 입력(get_pressed)
  keys = pygame.key.get_pressed()

  if keys[pygame.K_LEFT]:
    rect.x -= speed
  if keys[pygame.K_RIGHT]:
    rect.x += speed
  if keys[pygame.K_UP]:
    rect.y -= speed
  if keys[pygame.K_DOWN]:
    rect.y += speed

  # Rect 경계 처리
  if rect.left < 0:
    rect.left = 0
  if rect.right > WIDTH:
    rect.right = WIDTH
  if rect.top < 0:
    rect.top = 0
  if rect.bottom > HEIGHT:
    rect.bottom = HEIGHT

  screen.fill((200, 200, 200))   #추가: 화면 지우기

  pygame.draw.rect(screen, (255, 0, 0), (50, 50, 60, 60))   #추가: 빨간 사각형
  pygame.draw.circle(screen, (0, 255, 0), (200, 200), 30)   #추가: 초록 원
  pygame.draw.line(screen, (0, 0, 0), (0, 0), (100, 100), 3)  #추가: 검은 선

  screen.blit(img, rect)  # 네모 대신 이미지 그리기
  pygame.display.flip()

pygame.quit()