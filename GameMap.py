import pygame
import numpy as np
from Creature_components.Creatures import Creature
from Creature_components.Genes import Genes
from Config import *
from Food import Food
from Cell import Cell


class Map:
    def __init__(self, size_map):
        self.size_map = size_map
        self.cells_array = np.empty(size_map[::-1], dtype=object)
        self.size_cell = SIZE_CELL
        self.size_map_pix = (size_map[0] * self.size_cell, size_map[1] * self.size_cell)
        self.populate = 1
        self.cells_sprite = pygame.sprite.Group()
        self.agent_sprite = pygame.sprite.Group()
        self.food_sprite = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()
        self.border = self.create_border_map()
        self.count_creature = 0
        self.create_cell()
        self.create_agent()
        self.create_food()

    def create_cell(self):
        w, h = self.size_map
        for y in range(h):
            for x in range(w):
                cell = Cell(x * self.size_cell, y * self.size_cell)
                self.cells_array[y, x] = cell
                self.cells_sprite.add(cell)
                self.all_sprites.add(cell)

    def get_random_cell(self):
        w, h = self.size_map
        x = np.random.randint(w)
        y = np.random.randint(h)
        cell = self.cells_array[y, x]
        return cell, (y, x)

    def create_border_map(self):
        x, y = self.size_map_pix
        border_map = pygame.Rect(0, 0, x, y)
        return border_map

    @staticmethod
    def draw_border_map(screen, border):
        pygame.draw.rect(screen, (0, 0, 0), border, width=2)

    def create_agent(self):
        for i in range(self.populate):
            self.count_creature += 1
            cell, index_cell = self.get_random_cell()
            coord = cell.rect.topleft
            start_gen = Genes()
            agent = Creature(coord=coord, word_map=self.cells_array, index_cell=index_cell,
                             sprite_groups=(self.agent_sprite, self.all_sprites),
                             num=self.count_creature)
            agent.get_cell(cell)
            agent.get_gen(start_gen)
            agent.distribute_gen()
            # agent.create_logic()
            # agent.get_map(self.cells_array)
            cell.get_agent(agent)

    def create_food(self):
        spawn_food = 0
        while spawn_food < COUNT_FOOD:
            cell, index_cell = self.get_random_cell()
            if cell.food:
                continue
            else:
                coord = cell.rect.topleft
                food = Food(coord=coord,
                            index_cell=index_cell,
                            sprite_groups=(self.food_sprite, self.all_sprites),
                            cell=cell)
                food.get_map(self.cells_array)
                cell.get_food(food)
                spawn_food += 1
