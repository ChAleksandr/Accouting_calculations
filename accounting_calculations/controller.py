import pygame
import sys

screen_width = 800
screen_height = 600
clock = pygame.time.Clock()

pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption('Accounting Calculations')
icon = pygame.image.load(r'images/icon.png')
pygame.display.set_icon(icon)

game_state = 'main_menu'

text = ''

def events():
    global text

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_BACKSPACE:

                text = text[:-1]

            else:
                text += event.unicode

    clock.tick(60)
    return text

def game_exit():
    sys.exit()


def game_over():
    global game_state
    game_state = 'game_over'


def game_start():
    global game_state
    game_state = 'game_start'
