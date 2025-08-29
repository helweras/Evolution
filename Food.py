import pygame
import numpy as np
from Config import *
import time


class Food(pygame.sprite.Sprite):
    size = (SIZE_CELL, SIZE_CELL)
    age = 0

    def __init__(self, coord, index_cell, sprite_groups, cell=None):
        super().__init__(*sprite_groups)
        self.sprite_groups = sprite_groups
        self.index_cell_y, self.index_cell_x = index_cell
        self.x, self.y = coord
        self.image = pygame.Surface(self.size)
        self.rect = self.image.get_rect(topleft=coord)
        self.color = (0, 255, 0)
        self.image.fill(self.color)
        self.map = np.zeros(MAP_SIZE_CELL)
        self.cell = cell

        self.energy = 5
        self.age = 0
        self.time_life = 2

    def get_cell(self, cell):
        self.cell = cell

    def del_cell(self):
        self.cell = False

    def get_map(self, game_map):
        self.map = game_map

    def spore(self):
        x, y = self.rect.topleft
        coord = ((x, y + SIZE_CELL), (x, y - SIZE_CELL), (x + SIZE_CELL, y), (x - SIZE_CELL, y))
        spore = np.random.random()
        range_spore = 0
        if 0.2 < spore < 0.6:
            range_spore = 1
        elif 0.6 < spore < 0.85:
            range_spore = 2
        elif 0.85 < spore:
            range_spore = 3

        bord_x, bord_y = MAP_SIZE_PIX

        for i in range(range_spore):
            x_new, y_new = coord[i]
            if 0 <= x_new < bord_x and 0 <= y_new < bord_y:
                new_index_y = y_new // SIZE_CELL
                new_index_x = x_new // SIZE_CELL
                new_cell = self.map[new_index_y, new_index_x]
                if not new_cell.food:
                    index_new_cell = (new_index_y, new_index_x)
                    new_food = self.food_div(coord=coord[i],
                                             index_cell=index_new_cell,
                                             sprite_group=self.sprite_groups,
                                             cell=new_cell)
                    new_cell.get_food(new_food)
                    new_food.get_map(self.map)

    def food_div(self, coord, index_cell, sprite_group, cell=None):
        new = self.__class__(coord, index_cell, sprite_group, cell)
        return new

    def dead(self):
        self.cell.del_food()
        self.del_cell()
        self.kill()

    def update(self, dt):
        self.time_life -= dt
        self.energy += dt
        if self.time_life <= 0:
            self.spore()
            self.dead()
