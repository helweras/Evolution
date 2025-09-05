import pygame
import numpy
from random import choice


class NodeBase:

    def run(self, dt, creature, ctx):
        return 'переопределить'


class Node(NodeBase):
    def __init__(self, value, condition, behavior):
        self.node_true = None
        self.node_false = None
        self.value = value
        self.behavior = behavior
        self.condition = condition
        self.timer = 0

    def __repr__(self):
        return f"Узел {self.value}: {self.behavior} cond={self.condition.__name__}\n"

    def get_node(self, node_true, node_false):
        self.node_true = node_true
        self.node_false = node_false

    def run(self, dt, creature, ctx):
        return self.behavior.start(dt, creature, ctx)

    def left_right(self, creature):
        if self.condition(creature):
            return self.node_true
        else:
            return self.node_false
