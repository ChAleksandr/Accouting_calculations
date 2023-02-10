import sqlite3
import pygame
from menu_buttons import Button


class Workers:
    def __init__(self):
        conn = sqlite3.connect(r'tables/workers_cash.db')
        cursor = conn.cursor()
        cursor.execute("SELECT worker, cost, produce, mastery FROM workers")
        self.result = cursor.fetchall()
        self.alan_inf = self.result[3]
        self.petra_inf = self.result[2]
        self.john_inf = self.result[1]
        self.steve_inf = self.result[0]
        self.alan = pygame.image.load(r'images/workers_images/Alan.png').convert_alpha()
        self.petra = pygame.image.load(r'images/workers_images/Petra.png').convert_alpha()
        self.john = pygame.image.load(r'images/workers_images/John.png').convert_alpha()
        self.steve = pygame.image.load(r'images/workers_images/Steve.png').convert_alpha()

    def worker_dis(self, worker, pos, surface):
        if pos == 1:
            surface.blit(eval(f'self.{worker}'), (160, 250))
        elif pos == 2:
            surface.blit(eval(f'self.{worker}'), (540, 250))

    def get_mastery(self, worker):
        return int(eval(f'self.{worker}_inf')[3])

    def get_produce(self, worker):
        if worker != 'None':
            return eval(f'self.{worker}_inf')[2]
        return 0

    def info(self):
        return self.result
