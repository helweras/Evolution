from Node import Node
class DoIt:
    def __init__(self, node: Node):
        self.node = node
    def go(self, dt, creature):
        # print(f'doing---{self.node}')
        x = self.node.run(dt, creature)
        # print(self.node.behavior.creature)
        # print('time_for_action=',self.node.behavior.time_for_action)
        # print(x, '=x')
        if x:
            self.node = self.node.left_right(creature)



