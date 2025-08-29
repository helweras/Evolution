import pygame
from Node import Node
from random import choice
from Creature_components.ConditionCheck import Condition
from Creature_components.BehaviorBlocks import Behavior


class BuilderTree:
    def __init__(self, tree=None, root=None):
        self.behavior = Behavior()
        self.condition = Condition()
        if tree is None:
            self.tree_list = []
        self.tree_list = tree
        self.root = root

    def gen_tree(self, deep):
        if deep < 1:
            return None
        all_nodes = []
        value_counter = 1
        cond = choice(self.condition.check_list)
        act = choice(self.behavior.behavior_list)

        root = Node(value=value_counter, condition=cond, behavior=act)

        all_nodes.append(root)
        current_level = [root]

        for d in range(1, deep):
            next_level = []
            for node in current_level:
                cond_t = choice(self.condition.check_list)
                cond_f = choice(self.condition.check_list)
                act_t = choice(self.behavior.behavior_list)
                act_f = choice(self.behavior.behavior_list)

                value_counter += 1
                node_t = Node(value_counter, condition=cond_t, behavior=act_t)

                value_counter += 1
                node_f = Node(value_counter, condition=cond_f, behavior=act_f)

                node.get_node(node_t, node_f)
                all_nodes.extend([node_t, node_f])
                next_level.extend([node_t, node_f])

            current_level = next_level

        for node in current_level:
            node_true = choice(all_nodes)
            node_false = choice(all_nodes)
            node.get_node(node_true, node_false)
        self.tree_list = all_nodes
        self.root = root

    def get_root(self):
        return self.root

    def get_tree(self):
        return self.tree_list



    def print_behavior(self):
        print(*self.tree_list)
