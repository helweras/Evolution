

class Genes:
    def __init__(self):
        self.metabolic = {'energy':20}
        self.move_logic= {'speed': 5}
        self.reproduction = {'energy_for_mitoz': 30, 'offsprings': 1}
        self.color = (125, 125, 125)
        self.root = None
        self.tree = None

    def get_tree_and_root(self, tree, root):
        self.tree = tree
        self.root = root

    def __del__(self):
        print('smert gen')
