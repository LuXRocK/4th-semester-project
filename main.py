import pygame

pygame.init()
size = (1500, 900)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Title")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))