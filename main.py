import pygame
import pygame.display

pygame.init()

width = 1500
height = 900
size = (width, height)
screen = pygame.display.set_mode(size)

white = (255,255,255)
black = (0,0,0)
input_box_grey = (144, 150, 146)
input_box_green = (10, 194, 71)

username = ""
active = False
input_box = (200, 200, 140, 32)

pygame.display.set_caption("Title")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if 

    screen.fill(black)

    pygame.display.update()