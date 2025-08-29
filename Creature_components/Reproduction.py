import pygame
import numpy as np
import copy
import sys


class Reproduction:
    def __init__(self, creature):
        self.creature = creature
        self.energy_for_mitoz: int = None
        self.offsprings: int = None

    def split_up(self):
        for i in range(1):
            self.mitoz()

    def mitoz(self):
        print('start')
        new_gen: Genes = copy.copy(self.creature.return_gen())
        root = copy.copy(self.creature.logic.builder_tree.get_root())
        tree = copy.copy(self.creature.logic.builder_tree.get_tree())
        new_gen.get_tree_and_root(tree=tree, root=root)
        new_num = self.creature.my_number + 1

        new = self.creature.__class__(coord=self.creature.rect.topleft,
                                      index_cell=(self.creature.index_cell_y, self.creature.index_cell_x),
                                      word_map=self.creature.map,
                                      sprite_groups=self.creature.sprite_groups, num=new_num,
                                      )
        new.get_gen(new_gen)
        new.distribute_gen()
        new.get_cell(self.creature.cell)
        new.cell.get_agent(new)
        print('end')
        # print(new)
        # gen = {
        #     'color': self.creature.color.copy(),
        #     'speed': self.creature.speed,
        #     'life_time': self.creature.death_time
        # }
        # matrix_color = np.array(list(gen['color']))
        # d_color = np.random.randint(-7, 7, size=matrix_color.shape)
        # matrix_color = gen['color'] + d_color
        # matrix_color = np.clip(matrix_color, 0, 255).astype(np.uint8)
        #
        # gen['color'] = matrix_color
        # self.creature.kkal -= 10
        #
        # new = self.creature.__class__(self.creature.rect.topleft,
        #                               (self.creature.index_cell_y, self.creature.index_cell_x, self.creature.map),
        #                               self.creature.sprite_groups,
        #                               **gen)
        #
        # new.get_cell(self.creature.cell)
        # new.cell.get_agent(new)
        # new.get_map(self.creature.map)

    def get_gen(self, gen: str, val):
        if hasattr(self, gen):  # проверяем, что атрибут есть
            setattr(self, gen, val)  # присваиваем
        else:
            raise AttributeError(f"Нет атрибута '{gen}' ")
