import pygame
import numpy as np
import copy
import sys
import Config as conf
from Creature_components.Genes import Genes


class Reproduction:
    def __init__(self, creature):
        self.creature = creature
        self.energy_for_mitoz: int = None
        self.offsprings: int = None

    def split_up(self):
        for i in range(2):
            self.mitoz()

    def mitoz(self):
        new_gen = Genes(self.creature.return_gen())
        root = copy.copy(self.creature.logic.builder_tree.get_root())
        tree = copy.copy(self.creature.logic.builder_tree.get_tree())
        new_gen.get_tree_and_root(tree=tree, root=root)
        new_num = self.creature.my_number + 2

        new = self.creature.__class__(coord=self.creature.rect.topleft,
                                      index_cell=(self.creature.index_cell_y, self.creature.index_cell_x),
                                      word_map=self.creature.map,
                                      sprite_groups=self.creature.sprite_groups, num=new_num,
                                      )
        new.get_gen(new_gen)
        new.distribute_gen()
        new.get_cell(self.creature.cell)
        new.cell.get_agent(new)

    def get_gen(self, gen: str, val):
        if hasattr(self, gen):  # проверяем, что атрибут есть
            setattr(self, gen, val)  # присваиваем
        else:
            raise AttributeError(f"Нет атрибута '{gen}' ")
