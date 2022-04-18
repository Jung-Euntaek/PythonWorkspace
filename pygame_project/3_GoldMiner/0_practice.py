# import math

# rad_angle = math.radians(90)
# print(rad_angle) # 3.141592... / 2
# rad_angle = math.radians(180)
# print(rad_angle)

# import pygame
# print(pygame.font.get_fonts()

while True:
    width = int(input("width : "))
    height = int(input("height : "))
    mod_width, mod_height = int(960 * width / 1280), int(640 * height / 720)
    print(mod_width, mod_height)