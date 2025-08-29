import pygame
import numpy
from random import choice
import time


class Create:
    def __init__(self):
        self.death = 1
        self.time = 0


class Block:
    def run(self):
        pass


class BlockAction(Block):
    def __init__(self, condition, action):
        self.num = None
        self.act = action
        self.blok_true = None
        self.blok_false = None
        self.condition = condition
        self.block_list = []
        self.get_num()

    def run(self):
        self.act()
        if self.condition:
            self.blok_true.run()
        else:
            self.blok_false.run()

    def get_block(self, block_true, block_false):
        self.blok_true = block_true
        self.blok_false = block_false
        self.block_list = [block_true, block_false]

    def get_num(self):
        self.num = id(self)


class NodeBase:

    def run(self):
        return 'переопределить'


class Node(NodeBase):
    def __init__(self, value, condition, action):
        self.node_true = None
        self.node_false = None
        self.value = value
        self.action = action
        self.condition = condition

    def __repr__(self):
        return f"Узел{self.value} ------- {self.action}"

    def get_node(self, node_true, node_false):
        self.node_true = node_true
        self.node_false = node_false

    def run(self):
        self.action.run()
        if self.condition:
            self.node_true.run()
        else:
            self.node_false.run()

    def give_act_num(self):
        self.action.node = self.value


class Action:
    def __init__(self, num):
        self.num = num
        self.node = None

    def run(self):
        time.sleep(1)
        print(self.num)
        return self.num

    def get_node(self, node):
        self.node = node

    def __repr__(self):
        return f'я делаю {self.num}'


def build_act():
    return [Action(i) for i in ['eat', ' wait', 'find', 'mitoz', 'dead', 'sleep', 'fight']]


def build_cond():
    return [i // 2 == 0 for i in range(10)]


action_list = build_act()
cond_list = build_cond()


def act_skip():
    return True


def build_tree(deep):
    if deep < 1:
        return None
    all_nodes = []
    value_counter = 1
    cond = choice(cond_list)
    act = choice(action_list)

    root = Node(value=value_counter, condition=cond, action=act)
    root.give_act_num()

    all_nodes.append(root)
    current_level = [root]

    for d in range(1, deep):
        next_level = []
        for node in current_level:
            cond_t = choice(cond_list)
            cond_f = choice(cond_list)
            act_t = choice(action_list)
            act_f = choice(action_list)

            value_counter += 1
            node_t = Node(value_counter, condition=cond_t, action=act_t)
            node_t.give_act_num()

            value_counter += 1
            node_f = Node(value_counter, condition=cond_f, action=act_f)
            node_f.give_act_num()

            node.get_node(node_t, node_f)
            all_nodes.extend([node_t, node_f])
            next_level.extend([node_t, node_f])

        current_level = next_level

    for node in current_level:
        node_true = choice(all_nodes)
        node_false = choice(all_nodes)
        node.get_node(node_true, node_false)
    return root, all_nodes


r, nodes = build_tree(4)


for i in nodes:
    print(f'''
                        {i}
                 |                          |
             {i.node_true}       {i.node_false} ''')



