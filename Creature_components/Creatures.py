import pygame
import numpy as np
from Config import *
import random
import sys
import gc
import copy
from Creature_components.Logic import Logic
from Creature_components.Genes import Genes


class Creature(pygame.sprite.Sprite):
    size = (SIZE_CELL, SIZE_CELL)

    age = 0

    def __init__(self, coord, word_map: np.array, index_cell, sprite_groups, num):
        super().__init__(*sprite_groups)
        self.sprite_groups = sprite_groups
        self.index_cell_y, self.index_cell_x = index_cell
        self.x, self.y = coord
        self.image = pygame.Surface(self.size)
        self.rect = self.image.get_rect(topleft=coord)
        self.color = (125, 125, 125)
        self.gen:Genes = None
        self.cell = None
        self.map = word_map
        self.my_number = num
        self.logic = self.create_logic()

    def __repr__(self):
        return f'number is {self.my_number}'

    def __del__(self):
        print(f"{self} is dead")

    def get_number(self, num):
        self.my_number = num

    def create_logic(self):
        return Logic(self)

    def get_gen(self, gen):
        self.gen = gen

    def distribute_gen(self):
        self.logic.distribute_gen()


    def return_gen(self):
        return self.gen

    def get_cell(self, cell):
        self.cell = cell

    def get_map(self, game_map):
        self.map = game_map

    def update(self, dt):
        self.logic.update(dt)


    def update_position(self, new_x, new_y):
        self.rect.topleft = (new_x, new_y)


    def del_cell(self):
        self.cell = None

