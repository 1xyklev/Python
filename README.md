import pygame
import random

pygame.init()

WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Multi-Object Game with Collision")

clock = pygame.time.Clock()

# 🎵 사운드 추가: 충돌 시 재생될 사운드를 준비합니다.
# 주의: 'hit.wav' 파일이 코드 실행 폴더에 있어야 합니다.
try:
    hit_sound = pygame.mixer.Sound("hit.wav")
except pygame.error:
    print("경고: 'hit.wav' 파일을 찾을 수 없습니다. 사운드 없이 진행됩니다.")
    # 파일이 없을 경우 더미 객체로 대체하여 오류를 방지
    class DummySound:
        def play(self): pass
    hit_sound = DummySound()

# --------- Player Sprite ---------
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # 'dukbird.png' 파일이 없으면 기본 빨간색 사각형으로 대체
        try:
            self.image = pygame.image.load("dukbird.png").convert_alpha()
            self.image = pygame.transform.scale(self.image, (50, 50))
        except pygame.error:
            self.image = pygame.Surface((50, 50))
            self.image.fill((0, 0, 255)) # 파란색
            print("경고: 'dukbird.png' 파일을 찾을 수 없습니다. 기본 파란색 플레이어를 사용합니다.")

        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT // 2)
        self.speed = 3

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed

        # 화면 경계 제한
        self.rect.clamp_ip(screen.get_rect())

# --------- Enemy Sprite (여러 객체 생성 및 랜덤 움직임) ---------
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.image.fill((255, 80, 80)) # 적군: 빨간색
        self.rect = self.image.get_rect()

        # 랜덤 위치에서 시작
        self.rect.x = random.randint(0, WIDTH - 30)
        self.rect.y = random.randint(0, HEIGHT - 30)

        # 랜덤 이동 방향/속도 설정
        # 0이 아닌 속도를 보장하기 위해 -3~3 사이의 값 중 0을 제외하고 선택
        self.speed_x = random.choice([i for i in range(-3, 4) if i != 0])
        self.speed_y = random.choice([i for i in range(-3, 4) if i != 0])

    def update(self):
        # 움직임 (좌우, 위아래)
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        # 화면 벽에 부딪히면 튕기기
        if self.rect.left < 0 or self.rect.right > WIDTH:
            self.speed_x *= -1
        if self.rect.top < 0 or self.rect.bottom > HEIGHT:
            self.speed_y *= -1


# --------- 그룹 생성 및 객체 초기화 ---------
all_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group() # Enemy 객체만 따로 관리하는 그룹

player = Player()
all_sprites.add(player)

# ✅ 플레이어 외에 객체(Enemy) 5개 생성
for _ in range(5):
    e = Enemy()
    all_sprites.add(e)
    enemies.add(e)

# 충돌 변수 (점수) 초기화
score = 0
font = pygame.font.SysFont(None, 30)

# --------- 메인 루프 ---------
running = True
while running:
    # FPS 제어
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 모든 스프라이트 업데이트 (Player와 Enemy 모두 움직임)
    all_sprites.update()

    # ✅ 충돌 감지 및 변수 변경 (점수 증가)
    # pygame.sprite.spritecollide(스프라이트1, 그룹, 제거 여부)
    # False는 충돌해도 Enemy 객체를 제거하지 않음 (게임의 성격에 따라 True로 바꿀 수 있음)
    hit_list = pygame.sprite.spritecollide(player, enemies, False)

    if hit_list:
        # ✅ 사운드 재생
        hit_sound.play()

        # ✅ 변수 변경 (점수 증가)
        score += 1

        # 충돌한 적을 랜덤한 다른 위치로 이동시켜 게임 지속
        for h in hit_list:
            h.rect.x = random.randint(0, WIDTH - 30)
            h.rect.y = random.randint(0, HEIGHT - 30)
            # 충돌 시 움직임 방향도 재설정하여 플레이어가 연속으로 부딪히는 것을 방지
            h.speed_x = random.choice([i for i in range(-3, 4) if i != 0])
            h.speed_y = random.choice([i for i in range(-3, 4) if i != 0])

    # ---------------- 화면 출력 ----------------
    screen.fill((170, 200, 255))

    # 스프라이트 그리기 (Player와 Enemy 모두)
    all_sprites.draw(screen)

    # 점수 UI 출력
    text = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(text, (10, 10))

    pygame.display.flip()

pygame.quit()
