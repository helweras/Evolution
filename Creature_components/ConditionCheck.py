import pygame


class Condition:
    def __init__(self):
        self.check_list = (self.is_hungry, self.is_old)

    def is_hungry(self, creature):
        # print(f'is hungry --- {creature}')
        return creature.logic.metabolic.energy < 10

    def is_old(self, creature):
        # print(f'is old --- {creature}')
        return creature.logic.metabolic.energy > 3

    def is_dead(self, creature):
        return creature.logic.metabolic.energy <= 0

    
