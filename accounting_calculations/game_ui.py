import time

import pygame
import random
from tasks_difficulties import TasksAndDifficulties
from controller import screen, game_over, events
from menu_buttons import Button
from WORKERS import Workers
from stats import Stats


class BackGroundDisplay:
    def __init__(self, dis):
        self.count = -1
        self.bg = [
            pygame.image.load(r'images/back_ground_anim/game_background.png').convert_alpha()
                ]

    def animation_bg(self):
        self.count = (self.count + 0.08) % 1
        bg_img = self.bg[int(self.count)]
        bg_img = pygame.transform.scale(bg_img, (800, 600))
        return bg_img


add_img = pygame.image.load(r'images/buttons/add_btn.png').convert_alpha()
workers_list = pygame.image.load(r'images/workers_menu.png').convert_alpha()
alan_img = pygame.image.load(r'images/buttons/Alan_btn.png').convert_alpha()
petra_img = pygame.image.load(r'images/buttons/Petra_btn.png').convert_alpha()
steve_img = pygame.image.load(r'images/buttons/Steve_btn.png').convert_alpha()
john_img = pygame.image.load(r'images/buttons/John_btn.png').convert_alpha()
action_img = pygame.image.load(r'images/buttons/action_btn.png').convert_alpha()

alan_btn = Button(260, 295, alan_img, 0.5)
petra_btn = Button(260, 355, petra_img, 0.5)
steve_btn = Button(260, 420, steve_img, 0.5)
john_btn = Button(260, 485, john_img, 0.5)
alan_btn1 = Button(640, 295, alan_img, 0.5)
petra_btn1 = Button(640, 355, petra_img, 0.5)
steve_btn1 = Button(640, 420, steve_img, 0.5)
john_btn1 = Button(640, 485, john_img, 0.5)

poses1 = 160, 250
poses2 = 540, 250

timer = [0, 0]

tasks = [0, 0]

add_button = Button(160, 250, add_img, 2)
add_button2 = Button(540, 250, add_img, 2)
action_btn = Button(160, 100, action_img, 3)
action_btn2 = Button(540, 100, action_img, 3)
bg = BackGroundDisplay(screen)

w_s = Workers()
st = Stats()

cash = st.get('cash')
worker1 = st.get('worker1')
worker2 = st.get('worker2')


def main_game_draw():
    global worker1, worker2, cash
    text = events()
    screen.blit(bg.animation_bg(), (0, 0))
    if worker1 == 'None':
        if add_button.toggle_draw(screen):
            screen.blit(workers_list, poses1)
            if petra_btn.draw(screen) and int(cash) >= 2000:
                cash = int(cash) - 2000
                worker1 = 'petra'
            if john_btn.draw(screen) and int(cash) >= 5000:
                cash = int(cash) - 5000
                worker1 = 'john'
            if alan_btn.draw(screen) and int(cash) >= 3000:
                cash = int(cash) - 3000
                worker1 = 'alan'
            if steve_btn.draw(screen) and int(cash) >= 1000:
                cash = int(cash) - 1000
                worker1 = 'steve'
    else:
        w_s.worker_dis(worker1, 1, screen)
        timer[0] += random.randint(0, 4)
        if 1000 > timer[0] > 300:
            if action_btn.toggle_draw(screen):
                # cash = int(cash) + w_s.get_produce(worker1)
                screen.blit(tasks[0][2], (100, 200))
                if text == str(eval(tasks[0][1])):
                    timer[0] = 0
                    cash = int(cash) + w_s.get_produce(worker1)
                    action_btn.null_count()
            else:
                tasks[0] = TasksAndDifficulties(w_s.get_mastery(worker1), screen).mastery_check()
        elif 1000 < timer[0] < 2000:
            if random.randint(0, 4) < w_s.get_mastery(worker1):
                cash = int(cash) + w_s.get_produce(worker1)
                timer[0] = 0
            else:
                cash = int(cash) - w_s.get_produce(worker1)
                timer[0] = 0

    if worker2 == 'None':
        if add_button2.toggle_draw(screen):
            screen.blit(workers_list, poses2)
            if petra_btn1.draw(screen) and int(cash) >= 2000:
                cash = int(cash) - 2000
                worker2 = 'petra'
            if john_btn1.draw(screen) and int(cash) >= 5000:
                cash = int(cash) - 5000
                worker2 = 'john'
            if alan_btn1.draw(screen) and int(cash) >= 3000:
                cash = int(cash) - 3000
                worker2 = 'alan'
            if steve_btn1.draw(screen) and int(cash) >= 1000:
                cash = int(cash) - 1000
                worker2 = 'steve'
    else:
        w_s.worker_dis(worker2, 2, screen)
        timer[1] += random.randint(0, 4)
        if 500 > timer[1] > 300 or 1000 > timer[1] > 600:
            if action_btn2.toggle_draw(screen):
                # cash = int(cash) + w_s.get_produce(worker1)
                screen.blit(tasks[1][2], (500, 200))
                if text == str(eval(tasks[1][1])):
                    timer[1] = 0
                    cash = int(cash) + w_s.get_produce(worker2)
                    action_btn2.null_count()
            else:
                tasks[1] = TasksAndDifficulties(w_s.get_mastery(worker2), screen).mastery_check()
        elif 1000 < timer[1] < 2000:
            if random.randint(0, 4) < w_s.get_mastery(worker2):
                cash = int(cash) + w_s.get_produce(worker2)
                timer[1] = 0
            else:
                cash = int(cash) - w_s.get_produce(worker2)
                timer[1] = 0

    font2 = pygame.font.SysFont('didot.ttc', 50)
    img2 = font2.render(f"{str(cash)}$", True, '#006400')
    screen.blit(img2, (370, 20))

    text_surface = font2.render(text, True, (0, 0, 0))
    screen.blit(text_surface, (350, 100))

    pygame.display.flip()
    st.set('worker1', worker1)
    st.set('worker2', worker2)
    st.set('cash', cash)
    st.save()

    if int(cash) < 0:
        stats_file = open('statistic.csv', 'w', encoding='utf-8')
        stats_file.write(f"cash;1000\nworker1;None\nworker2;None")
        stats_file.close()
        game_over()

