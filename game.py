import pygame
from spritesheet import Spritesheet
from tiles import *
from menu import *


class Game():
    def __init__(self):
        pygame.init()
        self.running, self.playing = True, False
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False
        self.DISPLAY_W, self.DISPLAY_H = 1500, 900
        self.display = pygame.Surface((self.DISPLAY_W,self.DISPLAY_H))
        self.window = pygame.display.set_mode(((self.DISPLAY_W,self.DISPLAY_H)))
        self.font_name = '8bit_wonder/8-BIT WONDER.TTF'
        # self.font_name = pygame.font.get_default_font()
        self.BLACK, self.WHITE = (0, 0, 0), (255, 255, 255)
        self.main_menu = MainMenu(self)
        self.options = OptionsMenu(self)
        self.exit = Exit(self)
        self.curr_menu = self.main_menu
        self.spritesheet = Spritesheet('spritesheet.png')
        self.player_img = self.spritesheet.parse_sprite('chick.png')
        self.player_rect = self.player_img.get_rect()
        self.map = TileMap('level.csv', self.spritesheet )
        self.player_rect.x, self.player_rect.y = self.map.start_x, self.map.start_y


    def game_loop(self):
        while self.playing:
            self.check_events()
            if self.START_KEY:
                self.playing= False
            self.display.fill(self.BLACK)
            self.map.draw_map(self.display)
            self.display.blit(self.player_img, self.player_rect)
            self.window.blit(self.display, (0,0))
            self.reset_keys()
            pygame.display.update()



    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or self.curr_menu == self.exit:
                self.running, self.playing = False, False
                self.curr_menu.run_display = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.START_KEY = True
                if event.key == pygame.K_BACKSPACE:
                    self.BACK_KEY = True
                if event.key == pygame.K_DOWN:
                    self.DOWN_KEY = True
                if event.key == pygame.K_UP:
                    self.UP_KEY = True
                if event.key == pygame.K_ESCAPE:
                    self.running, self.playing = False, False
                    self.curr_menu.run_display = False

    def reset_keys(self):
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False

    def draw_text(self, text, size, x, y ):
        font = pygame.font.Font(self.font_name,size)
        text_surface = font.render(text, True, self.WHITE)
        text_rect = text_surface.get_rect()
        text_rect.center = (x,y)
        self.display.blit(text_surface,text_rect)




