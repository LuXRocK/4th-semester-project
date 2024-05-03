import pygame, sys, button, functions, variables

#Pygame setup
mainClock = pygame.time.Clock()
from pygame.locals import *
pygame.init()
pygame.display.set_caption("Looper")
screen = pygame.display.set_mode(variables.size)
font = pygame.font.SysFont(None, 32)

#Input box setup
input_rect_width = 100
input_rect_height = 50
input_rect = pygame.Rect(variables.width/2-input_rect_width/2, variables.height/2-input_rect_height/2, input_rect_width, input_rect_height)
color = variables.input_box_grey

enter_button = button.Button(variables.width/2-50, (2/3)*variables.height, variables.enter_img, 0.5)

def userSelect():
    username_input = ""
    active = False
    while True:



        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_rect.collidepoint(event.pos):
                    active = True
                else:
                    active = False
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if active == True:
                    if event.key == pygame.K_BACKSPACE:
                        username_input = username_input[:-1]
                    elif len(username_input) < 8:
                        username_input += event.unicode

        screen.fill(variables.black)
        functions.drawText("Enter username:", font, variables.white, screen, variables.width/2, variables.height/3)

        if active:
            color = variables.input_box_green
        else:
            color = variables.input_box_grey
    
        pygame.draw.rect(screen, color, input_rect, 2)

        text_surface = font.render(username_input, True, variables.white)
        screen.blit(text_surface, (input_rect.x + 5, input_rect.y + 15))
        input_rect.w = max(input_rect_width, text_surface.get_width() + 10)

        if enter_button.draw(screen):
            if len(username_input) > 0:
                user = functions.selectUser(variables.data_file_path, username_input)
                variables.username = user.split(' ')[0]
                variables.user_score = user.split(' ')[1]
                return 0 
        
        pygame.display.update()
        mainClock.tick(60)