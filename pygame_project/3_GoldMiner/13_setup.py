# 보석 다양하게 투입

import os
import math
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

    def update(self, to_x):
        if self.direction == LEFT: # 왼쪽 방향으로 이동한다면
            self.angle += self.angle_speed # 이동 속도만큼 각도 증가
        elif self.direction == RIGHT:
            self.angle -= self.angle_speed

        # 만약에 허용 각도 범위 벗어나면?
        if self.angle > 170:
            self.angle = 170
            self.set_direction(RIGHT)
        elif self.angle < 10:
            self.angle = 10
            self.set_direction(LEFT)

        self.offset.x += to_x

        self.rotate() # 회전 처리
        
    def rotate(self):
        self.image = pygame.transform.rotozoom(self.original_image, -self.angle, 1)
        # 회전 대상 이미지, 회전각 (아래로 회전하므로 -), 이미지 크기 변경
        offset_rotated = self.offset.rotate(self.angle) # rotate : 해당 벡터(Vector2) 값을 회전 시킨 벡터 값 반환
        self.rect = self.image.get_rect(center=self.position+offset_rotated)
        # 집게 이미지 회전 시 rect가 변하지 않으면 동떨어져 움직임
        # -> rect 변경시키고 중심을 변경되는 rect의 center로 맞춰주기

    def set_direction(self, direction):
        self.direction = direction

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        pygame.draw.line(screen, BLACK, self.position, self.rect.center, 5) # 직선 그리기

    def set_init_state(self):
        self.offset.x = default_offset_x_claw
        self.angle = 10
        self.direction = LEFT

# 보석 클래스
class Gemstone(pygame.sprite.Sprite):
    def __init__(self, image, position, price, speed):
        super().__init__()
        self.image = image
        self.rect = image.get_rect(center=position) # Sprite cls 상속 시 image와 rect 변수 반드시 정의
        self.price = price
        self.speed = speed

    def set_position(self, position, angle): # 집게 중심과 보석 중심 일치시키는 메소드
        r = self.rect.size[0] // 2 # 원 이미지로 간주 시 반지름과 동일
        rad_angle = math.radians(angle) # 각도
        to_x = r * math.cos(rad_angle) # 삼각형 밑변
        to_y = r * math.sin(rad_angle) # 삼각형 높이
        self.rect.center = (position[0] + to_x, position[1] + to_y)

def setup_gemstone():
    small_gold_price, small_gold_speed = 100, 5
    big_gold_price, big_gold_speed = 300, 2
    stone_price, stone_speed = 10, 2
    diamond_price, diamond_speed = 600, 7

    # 작은 금
    small_gold = Gemstone(gemstone_images[0], (150, 338), small_gold_price, small_gold_speed)
    gemstone_group.add(small_gold) # 그룹에 추가
    gemstone_group.add(Gemstone(gemstone_images[0], (300, 356), small_gold_price, small_gold_speed))
    gemstone_group.add(Gemstone(gemstone_images[0], (450, 400), small_gold_price, small_gold_speed))
    gemstone_group.add(Gemstone(gemstone_images[0], (650, 355), small_gold_price, small_gold_speed))
    gemstone_group.add(Gemstone(gemstone_images[0], (862, 337), small_gold_price, small_gold_speed))
    # 큰 금
    gemstone_group.add(Gemstone(gemstone_images[1], (225, 444), big_gold_price, big_gold_speed))
    gemstone_group.add(Gemstone(gemstone_images[1], (600, 444), big_gold_price, big_gold_speed))
    # 돌
    gemstone_group.add(Gemstone(gemstone_images[2], (225, 337), stone_price, stone_speed))
    gemstone_group.add(Gemstone(gemstone_images[2], (525, 293), stone_price, stone_speed))
    gemstone_group.add(Gemstone(gemstone_images[2], (750, 426), stone_price, stone_speed))
    # 다이아몬드
    gemstone_group.add(Gemstone(gemstone_images[3], (675, 373), diamond_price, diamond_speed))
    gemstone_group.add(Gemstone(gemstone_images[3], (112, 444), diamond_price, diamond_speed))

def update_score(score):
    global curr_score
    curr_score += score

def display_score():
    txt_curr_score = game_font.render(f"Curr Score : {curr_score:,}", True, BLACK)
    screen.blit(txt_curr_score, (38, 18))

    txt_goal_score = game_font.render(f"Goal Score : {goal_score:,}", True, BLACK)
    screen.blit(txt_goal_score, (38, 71))

def display_time(time):
    txt_timer = game_font.render(f"Time : {time}", True, BLACK)
    screen.blit(txt_timer, (810, 45))

def display_game_over():
    game_font = pygame.font.SysFont("arialrounded", 60) # 큰 폰트
    txt_game_over = game_font.render(game_result, True, BLACK)
    rect_game_over = txt_game_over.get_rect(center=(int(screen_width / 2), int(screen_height / 2))) # 화면 중앙에 표시
    screen.blit(txt_game_over, rect_game_over)

pygame.init()
screen_width = 960
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Gold Miner")
clock = pygame.time.Clock()
game_font = pygame.font.SysFont("arialrounded", 30)

# 점수 관련 변수
goal_score = 1500 # 목표 점수
curr_score = 0 # 현재 점수

# 게임 오버 관련 변수
game_result = None # 게임 결과
total_time = 60 # 총 시간
start_ticks = pygame.time.get_ticks() # 현재 tick 받아옴

# 게임 관련 변수
default_offset_x_claw = 30 # 중심점으로부터 집게까지의 기본 x 간격
to_x = 0 # x 좌표 기준으로 집게 이미지 이동시킬 값 저장 변수
caught_gemstone = None # 집게로 잡은 보석 정보

# 속도 변수
move_speed = 12 # 발사 시 이동 스피드 (x 좌표 기준으로 증가되는 값)
return_speed = 20 # 아무것도 없이 돌아올 때 스피드

# 방향 변수
LEFT = -1 # 왼쪽 방향
STOP = 0 # 이동 방향 좌우 아닌 고정 상태 (집게 뻗음)
RIGHT = 1 # 오른쪽 방향

# 색깔 변수
RED = (255, 0, 0) # 빨강
BLACK = (0, 0, 0) # 검정

# 배경 이미지 불러오기
current_path = os.path.dirname(__file__) # 현재 파일 위치 반환
background = pygame.image.load(os.path.join(current_path, "background.png"))

# 4개 보석 이미지 불러오기 (작은 금, 큰 금, 돌, 다이아몬드)
gemstone_images = [
    pygame.image.load(os.path.join(current_path, "small_gold.png")).convert_alpha(),
    pygame.image.load(os.path.join(current_path, "big_gold.png")).convert_alpha(),
    pygame.image.load(os.path.join(current_path, "stone.png")).convert_alpha(),
    pygame.image.load(os.path.join(current_path, "diamond.png")).convert_alpha()] # convert_alpha() : 이미지에 투명도 호출

# 보석 그룹
gemstone_group = pygame.sprite.Group()
setup_gemstone() # 게임에 원하는 만큼의 보석 정의

# 집게
claw_image = pygame.image.load(os.path.join(current_path, "claw.png")).convert_alpha()
claw = Claw(claw_image, (screen_width // 2, 98))

running = True
while running:
    clock.tick(30) # FPS 값 30으로 고정
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN: # 마우스 버튼 누를 때 집게 뻗음
            if claw.direction != STOP: # 집게가 좌우로 이동중일 때만 마우스 이벤트 처리
                claw.set_direction(STOP)
                to_x = move_speed # move_speed 의 속도로 집게 뻗음

    if claw.rect.left < 0 or claw.rect.right > screen_width or claw.rect.bottom > screen_height:
        to_x = -return_speed

    if claw.offset.x < default_offset_x_claw: # 원위치에 오면
        to_x = 0
        claw.set_init_state() # 처음 상태로 되돌림

        if caught_gemstone: # 잡힌 보석이 있다면
            update_score(caught_gemstone.price) # 점수 업데이트 처리
            gemstone_group.remove(caught_gemstone) # 그룹에서 잡힌 보석 제외
            caught_gemstone = None

    if not caught_gemstone: # 잡힌 보석 없다면 충돌 체크
        for gemstone in gemstone_group:
            # if claw.rect.colliderect(gemstone.rect): # 직사각형 기준 충돌 처리
            if pygame.sprite.collide_mask(claw, gemstone): # 투명 영역 제외하고 실제 이미지 영역에 대해 충돌 처리
                caught_gemstone = gemstone # 잡힌 보석
                to_x = -gemstone.speed # 잡힌 보석의 이동 속도
                break

    if caught_gemstone:
        caught_gemstone.set_position(claw.rect.center, claw.angle)

    screen.blit(background, (0, 0)) # 화면 좌상단부터 그리기

    gemstone_group.draw(screen) # 그룹 내 모든 스프라이트를 screen에 그림
    claw.update(to_x)
    claw.draw(screen)

    # 점수 정보 보여줌
    display_score()

    # 시간 계산
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000
    display_time(total_time - int(elapsed_time)) # 시간 표시

    # 만약에 시간이 8 이하이면 게임 종료
    if total_time - int(elapsed_time) <= 0:
        running = False
        if curr_score >= goal_score:
            game_result = "Mission Complete"
        else:
            game_result = "Game Over"
        # 게임 종료 메시지 표시
        display_game_over()        
    
    pygame.display.update()

pygame.time.delay(2000)
pygame.quit()