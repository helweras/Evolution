import pygame
import numpy as np
from Config import *
import random
import sys
import gc


class Creature(pygame.sprite.Sprite):
    def __init__(self, coord, index_cell, sprite_groups, cell=None):
        super().__init__(*sprite_groups)
        self.sprite_groups = sprite_groups
        self.x, self.y = coord
        self.size = (SIZE_CELL, SIZE_CELL)
        self.index_cell_y, self.index_cell_x = index_cell
        self.image = pygame.Surface(self.size)
        self.rect = self.image.get_rect(topleft=coord)
        self.speed = 4
        self.hp = 10
        self.food = 10
        self.start_setting(coord)
        self.cell = cell
        self.map = np.zeros(MAP_SIZE_CELL)
        self.age = 0
        self.death_time = 5.0

        self.move_delay = 1.0 / self.speed  # время между шагами
        self.move_timer = 0.0

    def start_setting(self, coord):
        self.image.fill((0, 255, 0))

    def get_cell(self, cell):
        self.cell = cell

    def get_map(self, game_map):
        self.map = game_map

    def update(self, dt):
        self.age += dt
        if self.age >= self.death_time:
            for i in range(2):
                self.mitoz()
            self.death()

        self.move_timer -= dt
        if self.move_timer <= 0:
            self.make_step()
            self.move_timer = self.move_delay

    def make_step(self):
        # АГЕНТ САМ ВЫБИРАЕТ направление
        direction = random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)])  # вниз, вверх, вправо, влево
        new_x = self.x + direction[0] * SIZE_CELL
        new_y = self.y + direction[1] * SIZE_CELL
        new_index_y = self.index_cell_y + direction[1]
        new_index_x = self.index_cell_x + direction[0]

        bord_x, bord_y = MAP_SIZE_PIX

        if 0 <= new_x < bord_x and 0 <= new_y < bord_y:
            try:
                self.x = new_x
                self.y = new_y
                self.index_cell_y = new_index_y
                self.index_cell_x = new_index_x
                cell = self.map[new_index_y, new_index_x]
                self.cell.del_agent(self)
                cell.get_agent(self)
                self.get_cell(cell)
                self.update_position(new_x, new_y)
            except Exception as e:
                print(e)
                sys.exit()

    def update_position(self, new_x, new_y):
        self.rect.topleft = (new_x, new_y)

    def death(self):
        self.cell.del_agent(self)
        self.kill()

    def mitoz(self):

        new = self.__class__(self.rect.topleft, (self.index_cell_y, self.index_cell_x), self.sprite_groups)
        new.get_cell(self.cell)
        new.cell.get_agent(new)
        new.get_map(self.map)
