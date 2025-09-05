import pygame


class Behavior:
    def __init__(self):
        self.find_food = FindFood()
        self.wait = Wait()
        self.mitoz = Mitoz()
        self.behavior_list = (self.find_food,)

    def get_behavior_list(self):
        return self.behavior_list


class AllBehavior:
    def __repr__(self):
        return f'{self.__class__.__name__}'

    def start(self, dt, creature, ctx):
        pass

    def get_name_creature(self, creature):
        print(f'creature {creature}')


class FindFood(AllBehavior):
    def __init__(self):
        super().__init__()

    def start(self, dt, creature, ctx):
        timer = ctx.timers["find_food"]
        timer -= dt
        creature.logic.move_logic.step(dt)
        if creature.cell.food or timer <= 0:
            creature.logic.metabolic.eat()
            ctx.timers["find_food"] = 1
            return True
        ctx.timers["find_food"] = timer
        return False


class Wait(AllBehavior):
    def __init__(self):
        super().__init__()

    def start(self, dt, creature, ctx):
        timer = ctx.timers["wait"]
        timer -= dt
        if creature.cell.food:
            creature.logic.metabolic.eat()
        creature.logic.metabolic.energy -= 0.5
        if timer <= 0:
            ctx.timers["wait"] = 1
            return True
        ctx.timers["wait"] = timer
        return False


class Mitoz(AllBehavior):
    def __init__(self):
        super().__init__()

    def start(self, dt, creature, ctx):
        creature.logic.reproduction.mitoz()
        creature.logic.metabolic.energy = 0
        return True
