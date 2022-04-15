import pygame

# 시작 화면 보여주기
def display_start_screen():
    pygame.draw.circle(screen, WHITE, start_button.center, 50, 5) # 그릴 곳, 색깔, 중심, 반지름, 두꼐

# 게임 화면 보여주기
def display_game_screen():
    print("Game Start")

# pos 에 해당하는 버튼 확인
def check_buttons(pos):
    global start
    if start_button.collidepoint(pos): # Rect 정보 내에 pos 위치하는지 확인 여부
        start = True # 변수를 그냥 사용하면 상관 없지만, 변수에 값 대입하기 위해서는 global 선언


# 초기화
pygame.init()
screen_width = 960
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Memory Game")

# 색깔
BLACK = (0, 0, 0) # RGB
WHITE = (255, 255, 255)

# 게임 시작 여부
start = False

# 시작 버튼
start_button = pygame.Rect(0, 0, 100, 100) # left, top, width, height
start_button.center = (100, screen_height - 100)

# 게임 루프
running = True # 게임 실행 여부
while running:
    click_pos = None

    # 이벤트 루프
    for event in pygame.event.get(): # 어떤 이벤트 발생?
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트인가?
            running = False
        elif event.type == pygame.MOUSEBUTTONUP: # 사용자가 마우스 클릭했을 때
            click_pos = pygame.mouse.get_pos() # 클릭 좌표 정보 호출

    # 화면 전체 까맣게 칠함
    screen.fill(BLACK)

    if start: # 게임 화면 표시
        display_game_screen()
    else:
        display_start_screen() # 시작 화면 표시

    # None 이 아니라면 (클릭을 했다면)
    if click_pos:
        check_buttons(click_pos)
        
    # 화면 업데이트
    pygame.display.update()

# 게임 종료
pygame.quit()