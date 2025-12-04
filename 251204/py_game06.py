#6. Surface와 Rect
import pygame

pygame.init()

WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Step 6")

# Surface 생성 + Rect 생성
# Surface: 그림이 그려지는 종이
# Rect: 위치/크기 정보 (충돌, 이동, 경계 처리도 담당)
img = pygame.Surface((40, 40))     # 추가: 네모 Surface 생성
img.fill((0, 0, 255))              # 추가: 파란색 채우기

rect = img.get_rect()              # 추가: rect 생성
rect.center = (WIDTH // 2, HEIGHT // 2)

speed = 1
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
    rect.x -= speed       # ← 기존 x 대신 rect.x 사용
  if keys[pygame.K_RIGHT]:
    rect.x += speed
  if keys[pygame.K_UP]:
    rect.y -= speed
  if keys[pygame.K_DOWN]:
    rect.y += speed

  # 추가: Rect는 경계를 쉽게 관리
  if rect.left < 0:
    rect.left = 0
  if rect.right > WIDTH:
    rect.right = WIDTH
  if rect.top < 0:
    rect.top = 0
  if rect.bottom > HEIGHT:
    rect.bottom = HEIGHT

  # 화면 그리기
  screen.fill((200, 200, 200))
  screen.blit(img, rect)     # ← 추가: Surface를 Rect 위치에 그리기

  pygame.display.flip()

pygame.quit()