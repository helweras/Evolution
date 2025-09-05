import pygame
import numpy as np
from Config import *
import random
import sys
import gc


class Metabolic:
    def __init__(self, creature):
        self.creature = creature
        self.energy: int = None

    def eat(self):
        if self.creature.cell.food:
            self.energy += self.creature.cell.food.energy
            self.creature.cell.food.dead()

    def death(self):
        try:
            self.creature.cell.del_agent(self.creature)
            self.creature.del_cell()
            self.creature.logic = None
            self.creature.kill()
        except Exception as e:
            print(f'{e}')

    def get_gen(self, gen: str, val):
        if hasattr(self, gen):  # проверяем, что атрибут есть
            setattr(self, gen, val)  # присваиваем
        else:
            raise AttributeError(f"Нет атрибута '{name}' ")
