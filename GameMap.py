import pygame
import numpy as np
from Creatures import Creature
from Config import *
import sys
import gc


class Cell(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.color = (255, 255, 255)
        self.image = pygame.Surface((SIZE_CELL, SIZE_CELL))
        self.image.fill(self.color)
        self.rect = self.image.get_rect(topleft=(x, y))
        self.show_border = False
        self.agent = []

    def toggle_border(self):
        self.show_border = not self.show_border
        self.draw_border()

    def draw_border(self):
        self.image.fill(self.color)
        if self.show_border:
            pygame.draw.rect(self.image, (0, 87, 84), self.image.get_rect(), 1)

    def del_agent(self, agent):
        self.agent.remove(agent)

    def get_agent(self, agent):
        self.color = (255, 0, 0)
        self.image.fill(self.color)
        self.agent.append(agent)

    def __str__(self):
        return f'{self.rect}'


class Map:
    def __init__(self, size_map):
        self.size_map = size_map
        self.cells_array = np.empty(size_map[::-1], dtype=object)
        self.size_cell = SIZE_CELL
        self.size_map_pix = (size_map[0] * self.size_cell, size_map[1] * self.size_cell)
        self.populate = 1
        self.cells_sprite = pygame.sprite.Group()
        self.agent_sprite = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()
        self.border = self.create_border_map()
        self.create_cell()
        self.create_agent()

    def create_cell(self):
        w, h = self.size_map
        for y in range(h):
            for x in range(w):
                cell = Cell(x * self.size_cell, y * self.size_cell)
                self.cells_array[y, x] = cell
                self.cells_sprite.add(cell)
                self.all_sprites.add(cell)

    def create_border_map(self):
        x, y = self.size_map_pix
        border_map = pygame.Rect(0, 0, x, y)
        return border_map

    @staticmethod
    def draw_border_map(screen, border):
        pygame.draw.rect(screen, (0, 0, 0), border, width=2)

    def create_agent(self):
        for i in range(self.populate):
            w, h = self.size_map
            x = np.random.randint(w)
            y = np.random.randint(h)
            coord = (x * self.size_cell, y * self.size_cell)
            cell = self.cells_array[y, x]
            agent = Creature(coord, (y, x), (self.agent_sprite, self.all_sprites))
            agent.get_cell(cell)
            agent.get_map(self.cells_array)
            cell.get_agent(agent)


