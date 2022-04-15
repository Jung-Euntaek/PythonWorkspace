import pygame

# 시작 화면 보여주기
def display_start_screen():
    pygame.draw.circle(screen, WHITE, start_button.center, 50, 5) # 그릴 곳, 색깔, 중심, 반지름, 두꼐

# 초기화
pygame.init()
screen_width = 960
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Memory Game")

# 색깔
BLACK = (0, 0, 0) # RGB
WHITE = (255, 255, 255)

# 시작 버튼
start_button = pygame.Rect(0, 0, 100, 100) # left, top, width, height
start_button.center = (100, screen_height - 100)

# 게임 루프
running = True # 게임 실행 여부
while running:
    # 이벤트 루프
    for event in pygame.event.get(): # 어떤 이벤트 발생?
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트인가?
            running = False

    # 화면 전체 까맣게 칠함
    screen.fill(BLACK)

    # 시작 화면 표시
    display_start_screen()

    # 화면 업데이트
    pygame.display.update()

# 게임 종료
pygame.quit()