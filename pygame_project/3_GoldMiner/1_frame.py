import pygame

pygame.init()
screen_width = 960
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Gold Miner")

clock = pygame.time.Clock()

running = True
while running:
    clock.tick(30) # FPS 값 30으로 고정
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()