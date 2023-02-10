import pygame
from controller import screen, game_exit
from menu_buttons import Button


class BackGroundDisplay:
    def __init__(self, dis):
        self.count = -1
        self.bg = [
            pygame.image.load(r'images/game_over3.png').convert_alpha(),
            pygame.image.load(r'images/game_over2.png').convert_alpha()
                ]

    def animation_bg(self):
        self.count = (self.count + 0.08) % 2
        bg_img = self.bg[int(self.count)]
        return bg_img


exit_img = pygame.image.load(r'images/buttons/exit_btn.png').convert_alpha()

exit_button = Button(330, 250, exit_img, 0.5)
bg = BackGroundDisplay(screen)


def game_over_draw():
    screen.blit(bg.animation_bg(), (300, 150))
    if exit_button.draw(screen):
        game_exit()
    pygame.display.flip()

