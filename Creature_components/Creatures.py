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
        self.image.fill(self.color)
        for key, val in self.gen.__dict__.items():
            if isinstance(val, dict):
                atr = self.logic.__dict__[key]
                for key_atr, val_atr in val.items():
                    atr.get_gen(key_atr, val_atr)
        self.logic.gen_tree(self.gen.tree, self.gen.root)
        self.logic.create_doit()

    def return_gen(self):
        return self.gen

    def get_cell(self, cell):
        self.cell = cell

    def get_map(self, game_map):
        self.map = game_map

    def update(self, dt):
        self.logic.update(dt)

    # def eat(self):
    #     if self.cell.food:
    #         self.kkal += self.cell.food.energy
    #         self.cell.food.dead()

    def update_position(self, new_x, new_y):
        self.rect.topleft = (new_x, new_y)

    def death(self):
        try:
            self.cell.del_agent(self)
            self.del_cell()
            self.kill()
        except Exception as e:
            print(f'{e}')
            sys.exit()

    def mitoz(self):
        gen = {
            'color': self.color.copy(),
            'speed': self.speed,
            'life_time': self.death_time
        }
        matrix_color = np.array(list(gen['color']))
        d_color = np.random.randint(-7, 7, size=matrix_color.shape)
        matrix_color = gen['color'] + d_color
        matrix_color = np.clip(matrix_color, 0, 255).astype(np.uint8)

        gen['color'] = matrix_color
        self.kkal -= 10

        new = self.__class__(self.rect.topleft,
                             (self.index_cell_y, self.index_cell_x),
                             self.sprite_groups,
                             **gen)

        new.get_cell(self.cell)
        new.cell.get_agent(new)
        new.get_map(self.map)

    def del_cell(self):
        self.cell = None

        # if self.check_death():
        #     self.death()
        #     return
        # self.age += dt
        # self.kkal -= dt * self.speed * 0.2
        # if self.age >= self.mitoz_age and self.check_mitoz():
        #     for i in range(1):
        #         self.mitoz()
