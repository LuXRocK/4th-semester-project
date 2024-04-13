import pygame
import sys
import button

pygame.init()

clock = pygame.time.Clock()

width = 1500
height = 900
input_rect_width = 100
input_rect_height = 50
size = (width, height)
screen = pygame.display.set_mode(size)

white = (255,255,255)
black = (0,0,0)
input_box_grey = (144, 150, 146)
input_box_green = (10, 194, 71)

base_font = pygame.font.Font(None, 32)
username = ""
wellcome_text = "Wellcome to the game, enter your name:"

input_rect = pygame.Rect(width/2-input_rect_width/2, height/2-input_rect_height/2, input_rect_width, input_rect_height)
color = input_box_grey
active = False

enter_img_path = 'sprites/enter_btn_white.png'
enter_img = pygame.image.load(enter_img_path).convert_alpha()


enter_button = button.Button(100, 200, enter_img, 0.5)

pygame.display.set_caption("Title")


while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

  
        if event.type == pygame.MOUSEBUTTONDOWN:
            if input_rect.collidepoint(event.pos):
                active = True
            else:
                active = False

        if event.type == pygame.KEYDOWN:
            if active == True:
                if event.key == pygame.K_BACKSPACE:
                    username = username[:-1]
                elif len(username) < 8:
                    username += event.unicode
    
    screen.fill(black)

    if active:
        color = input_box_green
    else:
        color = input_box_grey

    pygame.draw.rect(screen, color, input_rect, 2)
    if enter_button.draw(screen):
        print('ENTER')
        pygame.quit()
        

    wellcome_text_surface = base_font.render(wellcome_text, True, white)
    screen.blit(wellcome_text_surface, (width/2-wellcome_text_surface.get_width()/2, height/2-2*input_rect_height))
    text_surface = base_font.render(username, True, white)
    screen.blit(text_surface, (input_rect.x + 5, input_rect.y + 15))
    input_rect.w = max(input_rect_width, text_surface.get_width() + 10)

    pygame.display.flip()

    clock.tick(60)