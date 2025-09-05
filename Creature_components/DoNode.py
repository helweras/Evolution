from Node import Node


class DoIt:
    def __init__(self, node: Node):
        self.node = node

    def go(self, dt, creature, ctx):
        if self.node.run(dt, creature, ctx):
            self.node = self.node.left_right(creature)
