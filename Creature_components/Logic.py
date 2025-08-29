import pygame
import numpy as np
from Config import *
import random
import sys
import gc
import copy
from Creature_components.MovementLogic import MovementLogic
from Creature_components.Metabolizm import Metabolic
from Creature_components.Reproduction import Reproduction
from Creature_components.BuilderTree import BuilderTree
from Creature_components.DoNode import DoIt
class Logic:
    def __init__(self, creature):
        self.creature = creature
        self.move_logic = MovementLogic(self.creature)
        self.metabolic = Metabolic(self.creature)
        self.reproduction = Reproduction(self.creature)
        self.builder_tree:BuilderTree = None
        # self.builder_tree.print_behavior()
        self.doit:DoIt = None

    def __del__(self):
        print('logic_dead')

    def gen_tree(self, tree=None, root=None):
        build_tree = BuilderTree(tree=tree, root=root)
        if tree is None and root is None:
            build_tree.gen_tree(2)
        self.builder_tree = build_tree



    def create_doit(self):
        root = self.builder_tree.get_root()
        self.doit = DoIt(root)

    def update(self, dt):
        if self.builder_tree.condition.is_dead(self.creature):
            self.metabolic.death()
            return
        self.doit.go(dt, self.creature)
