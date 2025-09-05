import pygame
import numpy as np
from Config import *
import random
import sys
import gc
import copy


class MovementLogic:
    def __init__(self, creature):
        self.creature = creature
        self.move_timer = 0
        self.move_delay = 0.1
        self.speed: int = None

    def step(self, dt):
        if self.check_timer(dt):
            # АГЕНТ САМ ВЫБИРАЕТ направление
            direction = random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)])  # вниз, вверх, вправо, влево
            new_x = self.creature.x + direction[0] * SIZE_CELL
            new_y = self.creature.y + direction[1] * SIZE_CELL
            new_index_y = self.creature.index_cell_y + direction[1]
            new_index_x = self.creature.index_cell_x + direction[0]

            bord_x, bord_y = MAP_SIZE_PIX

            if self.check_border(new_x, new_y, bord_x, bord_y):
                try:
                    self.creature.x = new_x
                    self.creature.y = new_y
                    self.creature.index_cell_y = new_index_y
                    self.creature.index_cell_x = new_index_x
                    cell = self.creature.map[new_index_y, new_index_x]
                    self.creature.cell.del_agent(self.creature)
                    cell.get_agent(self.creature)
                    self.creature.get_cell(cell)
                    self.creature.update_position(new_x, new_y)
                    self.creature.logic.metabolic.energy -= 1
                except Exception as e:
                    print(e, 'step')
                    sys.exit()
            self.move_timer = 0

    def get_gen(self, gen: str, val):
        if hasattr(self, gen):  # проверяем, что атрибут есть
            setattr(self, gen, val)  # присваиваем
        else:
            raise AttributeError(f"Нет атрибута '{gen}' ")

    @staticmethod
    def check_border(x, y, bord_x, bord_y):
        return 0 <= x < bord_x and 0 <= y < bord_y

    def check_timer(self, dt):
        self.move_timer += dt
        return self.move_timer >= self.move_delay
