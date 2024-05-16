import pygame, sys, button, functions, user_select, variables

mainClock = pygame.time.Clock()
from pygame.locals import *
pygame.init()
pygame.display.set_caption("Looper")
screen = pygame.display.set_mode(variables.size)
font = pygame.font.SysFont(None, 32)


def scoreboard():

    while True:

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
  
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
        