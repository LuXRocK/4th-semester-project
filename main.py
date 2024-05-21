import user_select
from game import Game

g = Game()
user_select.userSelect()

while g.running:
    g.curr_menu.display_menu()
    g.game_loop()