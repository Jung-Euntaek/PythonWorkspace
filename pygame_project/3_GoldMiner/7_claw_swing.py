# 집게를 좌우로 이동
import os
import pygame

# 집게 클래스
class Claw(pygame.sprite.Sprite):
    def __init__(self, image, position):
        super().__init__()
        self.image = image # 지속적으로 변경될 이미지
        self.original_image = image # 원본 이미지
        self.rect = image.get_rect(center=position)

        self.offset = pygame.math.Vector2(default_offset_x_claw, 0)
        self.position = position # 최초 집게 중심

        self.direction = LEFT # 집게 이동 방향
        self.angle_speed = 2.5 # 집게의 각도 변경 폭 (좌우 이동 속도)
        self.angle = 10 # 최초 각도 정의 (오른쪽 끝)

    def update(self):
        if self.direction == LEFT: # 왼쪽 방향으로 이동한다면
            self.angle += self.angle_speed # 이동 속도만큼 각도 증가
        elif self.direction == RIGHT:
            self.angle -= self.angle_speed

        # 만약에 허용 각도 범위 벗어나면?
        if self.angle > 170:
            self.angle = 170
            self.direction = RIGHT
        elif self.angle < 10:
            self.angle = 10
            self.direction = LEFT

        self.rotate() # 회전 처리

        # print(self.angle, self.direction)
        
        # rect_center = self.position + self.offset # 이동한 집게 중심
        # self.rect = self.image.get_rect(center=rect_center)

    def rotate(self):
        self.image = pygame.transform.rotozoom(self.original_image, -self.angle, 1)
        # 회전 대상 이미지, 회전각 (아래로 회전하므로 -), 이미지 크기 변경

        offset_rotated = self.offset.rotate(self.angle) # rotate : 해당 벡터(Vector2) 값을 회전 시킨 벡터 값 반환

        self.rect = self.image.get_rect(center=self.position+offset_rotated)
        # 집게 이미지 회전 시 rect가 변하지 않으면 동떨어져 움직임
        # -> rect 변경시키고 중심을 변경되는 rect의 center로 맞춰주기

        # print(self.rect)
        pygame.draw.rect(screen, RED, self.rect, 1)

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        pygame.draw.circle(screen, RED, self.position, 3) # 중심점 표시
        pygame.draw.line(screen, BLACK, self.position, self.rect.center, 5) # 직선 그리기

# 보석 클래스
class Gemstone(pygame.sprite.Sprite):
    def __init__(self, image, position):
        super().__init__()
        self.image = image
        self.rect = image.get_rect(center=position) # Sprite cls 상속 시 image와 rect 변수 반드시 정의


def setup_gemstone():
    # 작은 금
    small_gold = Gemstone(gemstone_images[0], (200, 380))
    gemstone_group.add(small_gold) # 그룹에 추가
    # 큰 금
    gemstone_group.add(Gemstone(gemstone_images[1], (300, 500)))
    # 돌
    gemstone_group.add(Gemstone(gemstone_images[2], (300, 380)))
    # 다이아몬드
    gemstone_group.add(Gemstone(gemstone_images[3], (900, 420)))

pygame.init()
screen_width = 960
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Gold Miner")
clock = pygame.time.Clock()

# 게임 관련 변수
default_offset_x_claw = 30 # 중심점으로부터 집게까지의 기본 x 간격
LEFT = -1 # 왼쪽 방향
RIGHT = 1 # 오른쪽 방향

# 색깔 변수
RED = (255, 0, 0) # 빨강
BLACK = (0, 0, 0) # 검정

# 배경 이미지 불러오기
current_path = os.path.dirname(__file__) # 현재 파일 위치 반환
background = pygame.image.load(os.path.join(current_path, "background.png"))

# 4개 보석 이미지 불러오기 (작은 금, 큰 금, 돌, 다이아몬드)
gemstone_images = [
    pygame.image.load(os.path.join(current_path, "small_gold.png")),
    pygame.image.load(os.path.join(current_path, "big_gold.png")),
    pygame.image.load(os.path.join(current_path, "stone.png")),
    pygame.image.load(os.path.join(current_path, "diamond.png"))]

# 보석 그룹
gemstone_group = pygame.sprite.Group()
setup_gemstone() # 게임에 원하는 만큼의 보석 정의

# 집게
claw_image = pygame.image.load(os.path.join(current_path, "claw.png"))
claw = Claw(claw_image, (screen_width // 2, 98))

running = True
while running:
    clock.tick(30) # FPS 값 30으로 고정
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(background, (0, 0)) # 화면 좌상단부터 그리기

    gemstone_group.draw(screen) # 그룹 내 모든 스프라이트를 screen에 그림
    claw.update()
    claw.draw(screen)
    
    pygame.display.update()

pygame.quit()