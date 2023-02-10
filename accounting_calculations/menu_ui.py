import pygame
from controller import screen, game_exit, game_start
from menu_buttons import Button


class BackGroundDisplay:
    def __init__(self, dis):
        self.count = -1
        self.bg = [
            pygame.image.load(r'images/back_ground_anim/background_img0.png').convert_alpha(),
            pygame.image.load(r'images/back_ground_anim/background_img1.png').convert_alpha(),
            pygame.image.load(r'images/back_ground_anim/background_img2.png').convert_alpha(),
            pygame.image.load(r'images/back_ground_anim/background_img3.png').convert_alpha()
                ]

    def animation_bg(self):
        self.count = (self.count + 0.08) % 4
        bg_img = self.bg[int(self.count)]
        bg_img = pygame.transform.scale(bg_img, (800, 600))
        return bg_img


play_img = pygame.image.load(r'images/buttons/start_btn.png').convert_alpha()
exit_img = pygame.image.load(r'images/buttons/exit_btn.png').convert_alpha()

play_button = Button(173, 250, play_img, 0.6)
exit_button = Button(173, 400, exit_img, 0.6)
bg = BackGroundDisplay(screen)


def main_menu_draw():
    screen.blit(bg.animation_bg(), (0, 0))
    if play_button.draw(screen):
        game_start()
    if exit_button.draw(screen):
        game_exit()
    pygame.display.flip()

