from menu_ui import main_menu_draw
from game_ui import main_game_draw
from game_over_ui import game_over_draw
import controller

if __name__ == "__main__":
    while True:
        controller.events()
        if controller.game_state == 'main_menu':
            main_menu_draw()
        elif controller.game_state == 'game_start':
            main_game_draw()
        elif controller.game_state == 'game_over':
            game_over_draw()
