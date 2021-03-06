import pygame

# 초기화
pygame.init()
screen_width = 960
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Memory Game")

# 게임 루프
running = True # 게임 실행 여부
while running:
    # 이벤트 루프
    for event in pygame.event.get(): # 어떤 이벤트 발생?
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트인가?
            running = False

# 게임 종료
pygame.quit()