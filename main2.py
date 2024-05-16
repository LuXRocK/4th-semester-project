import pygame, sys, button, functions, user_select, variables, main_menu

mainClock = pygame.time.Clock()
from pygame.locals import *
pygame.init()
pygame.display.set_caption("Looper")
screen = pygame.display.set_mode(variables.size)
font = pygame.font.SysFont(None, 32)

while True:
    user_select.userSelect()

    main_menu.mainMenu()


# user_select.userSelect()

