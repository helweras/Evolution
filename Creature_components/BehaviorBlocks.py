import pygame


class Behavior:
    def __init__(self):
        self.find_food = FindFood()
        self.wait = Wait()
        self.mitoz = Mitoz()
        self.behavior_list = (self.mitoz,)

    def get_behavior_list(self):
        return self.behavior_list


class AllBehavior:
    def __init__(self):
        self.time_for_action = 2

    def __repr__(self):
        return f'{self.__class__.__name__}'

    def get_name_creature(self, creature):
        print(f'creature ')


class FindFood(AllBehavior):
    def __init__(self):
        super().__init__()
        self.time_for_action = 1

    def start(self, dt, creature):
        self.time_for_action -= dt
        creature.logic.move_logic.step(dt)
        if creature.cell.food:
            creature.logic.metabolic.eat()
            return True
        if self.time_for_action <= 0:
            self.time_for_action = 1
            return True
        return False


class Wait(AllBehavior):
    def __init__(self):
        super().__init__()

    def start(self, dt, creature):
        if creature.cell.food:
            creature.logic.metabolic.eat()
        self.time_for_action -= dt
        creature.logic.metabolic.energy -= 0.05
        if self.time_for_action <= 0:
            self.time_for_action = 1
            return True
        return False


class Mitoz(AllBehavior):
    def __init__(self):
        super().__init__()

    def start(self, dt, creature):
        self.time_for_action -= dt
        # if creature.logic.metabolic.energy >= 20:
        if self.time_for_action <= 0:
            creature.logic.reproduction.mitoz()
            creature.logic.metabolic.energy = 0
            self.time_for_action = 2
            return True
        return True
