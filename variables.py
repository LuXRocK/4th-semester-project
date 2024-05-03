import pygame

#window info
clock = pygame.time.Clock()
width = 1500
height = 900
size = (width, height)
screen = pygame.display.set_mode(size)

#colors
white = (255,255,255)
black = (0,0,0)
input_box_grey = (144, 150, 146)
input_box_green = (10, 194, 71)

# #fonts
# base_font = pygame.font.Font(None, 32)

#texts
username_input = ""
wellcome_text = "Wellcome to the game, enter your name:"

#user info
username = ""
user_score = ""

#paths
enter_img_path = 'sprites/enter_btn_white.png'
data_file_path = "users.txt"

#images
enter_img = pygame.image.load(enter_img_path).convert_alpha()
bg = pygame.image.load('sprites/bg1.png')

#still thinking
input_rect_width = 100
input_rect_height = 50
input_rect = pygame.Rect(width/2-input_rect_width/2, height/2-input_rect_height/2, input_rect_width, input_rect_height)
color = input_box_grey
active = False

# enter_button = button.Button(width/2-50, (2/3)*height, enter_img, 0.5)