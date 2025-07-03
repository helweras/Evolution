import pygame
import numpy
from Config import *


class Creature(pygame.sprite.Sprite):
    def __init__(self, coord):
        super().__init__()
        self.size = (SIZE_CELL, SIZE_CELL)
        self.image = None
        self.rect = None
        self.speed = 1
        self.hp = 10
        self.food = 10
        self.start_setting(coord)

    def start_setting(self, coord):
        self.image = pygame.Surface(self.size)
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect(topleft=coord)
