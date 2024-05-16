import pygame, sys, button, functions, user_select, variables

mainClock = pygame.time.Clock()
from pygame.locals import *
pygame.init()
pygame.display.set_caption("Looper")
screen = pygame.display.set_mode(variables.size)
font = pygame.font.SysFont(None, 32)

start_button = button.Button(variables.width/2-80, variables.height/3, variables.start_button, 1)
score_button = button.Button(variables.width/2-100, variables.height/2, variables.scoreboard_button, 1)
exit_button = button.Button(variables.width/2-40, variables.height*2/3, variables.exit_button, 1)

def mainMenu():

    while True:

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
  
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        screen.fill(variables.black)
        # functions.drawText("PLAY", font, variables.white, screen, variables.width/2, variables.height/3)
        start_button.draw(screen)
        # functions.drawText("SCOREBOARD", font, variables.white, screen, variables.width/2, variables.height/2)
        if score_button.draw(screen):
            pass
        # functions.drawText("EXIT", font, variables.white, screen, variables.width/2, variables.height*2/3)
        if exit_button.draw(screen):
            pygame.quit()
            sys.exit()
        functions.drawText("USER: " + variables.username, font, variables.white, screen, 150, 20)
        functions.drawText("SCORE: " + variables.user_score, font, variables.white, screen, 150, 40)

        pygame.display.update()

