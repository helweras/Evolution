import pygame
import numpy as np
from Config import *
import random
import sys
import gc
import copy


class Cell(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.color = (255, 255, 255)
        self.image = pygame.Surface((SIZE_CELL, SIZE_CELL))
        self.image.fill(self.color)
        self.rect = self.image.get_rect(topleft=(x, y))
        self.show_border = False
        self.agent = []
        self.food = False

    def toggle_border(self):
        self.show_border = not self.show_border
        self.draw_border()

    def draw_border(self):
        self.image.fill(self.color)
        if self.show_border:
            pygame.draw.rect(self.image, (0, 87, 84), self.image.get_rect(), 1)

    def del_agent(self, agent):
        try:
            self.agent.remove(agent)
        except Exception as e:
            print(e)
            print('del agent')


    def get_agent(self, agent):
        # self.color = (255, 0, 0)
        # self.image.fill(self.color)
        self.agent.append(agent)

    def get_food(self, food):
        self.food = food


    def del_food(self):
        self.food = False

    def __str__(self):
        return f'{self.rect}'
