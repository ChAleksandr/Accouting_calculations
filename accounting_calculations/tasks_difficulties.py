import random
import pygame


class TasksAndDifficulties:
    def __init__(self, mastery, dis):
        self.dis = dis
        self.mastery = mastery
        self.data = "None"
        self.easy = [
            "Какой доход на данный момент?",
            "Сколько работников?"
        ]
        self.medium = [
            "Какой оклад приносит 1 работник?",
            "Какой оклад приносит 2 работник"
        ]

        self.hard = [
            "Какой доход на данный момент?",
            "Сколько работников?",
            "Какой оклад приносит 1 работник?",
            "Какой оклад приносит 2 работник"
        ]

        self.easy_answers = [
            "w_s.get_produce(worker1) + w_s.get_produce(worker2)",
            "[worker1, worker2].count(not 'None')"
        ]

        self.medium_answers = [
            "w_s.get_produce(worker1)",
            "w_s.get_produce(worker2)"
        ]

        self.hard_answers = [
            "w_s.get_produce(worker1) + w_s.get_produce(worker2)",
            "[worker1, worker2].count('None')",
            "w_s.get_produce(worker1)",
            "w_s.get_produce(worker2)"
        ]

    def mastery_check(self):
        if self.mastery < 2:
            return self.easy_task()
        elif self.mastery == 2:
            return self.medium_task()
        else:
            return self.hard_task()

    def easy_task(self):
        con = random.randint(0, 1)
        task = self.easy[con]
        font = pygame.font.SysFont('didot.ttc', 30)
        img = font.render(task, True, 'WHITE')
        if self.data == "None":
            self.data = task, self.easy_answers[con], img
            return task, self.easy_answers[con], img
        return self.data

    def medium_task(self):
        con = random.randint(0, 1)
        task = self.medium[con]
        font = pygame.font.SysFont('didot.ttc', 30)
        img = font.render(task, True, 'WHITE')
        if self.data == "None":
            self.data = task, self.medium_answers[con], img
            return task, self.medium_answers[con], img
        return self.data

    def hard_task(self):
        con = random.randint(0, 3)
        task = self.hard[con]
        font = pygame.font.SysFont('didot.ttc', 30)
        img = font.render(task, True, 'WHITE')
        if self.data == "None":
            self.data = task, self.hard_answers[con], img
            return task, self.hard_answers[con], img
        return self.data
