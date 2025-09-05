import numpy as np


class Genes:
    def __init__(self, gen=None):
        if not gen:
            self.genes = {
                "metabolic": {"energy": 20},
                "move_logic": {"speed": 5.0},
                "reproduction": {"energy_for_mitoz": 30, "offsprings": 1},
            }
        else:
            self.genes = {key:value.copy() for key, value in gen.genes.items()}

        self.color = (125, 125, 125)
        self.root = None
        self.tree = None

        self.param_order = self.build_param_order()


    def build_param_order(self):
        """Создаёт список пар (блок, ключ) для всех параметров"""
        order = [
            (block, key)
            for block, params in self.genes.items()
            for key in params
        ]
        return order

    def to_array_all(self):
        """
            Преобразует все гены всех блоков в один плоский numpy-массив.

            Используется для векторных операций на всех параметрах одновременно.

            Returns:
                np.ndarray: Массив всех значений генов в порядке self.param_order.
            """
        return np.array([self.genes[d][k] for d, k in self.param_order], dtype=np.float32)

    def from_array_all(self, arr):
        """
            Обновляет все блоки генов из плоского numpy-массива.

            Значения распределяются по блокам и ключам согласно self.param_order.

            Args:
                arr (np.ndarray): Массив значений, соответствующий порядку self.param_order.
            """
        for (d, k), value in zip(self.param_order, arr):
            self.genes[d][k] = value

    def to_array_gen(self, gen_name: str):
        """
            Преобразует выбранный блок генов в numpy-массив.

            Args:
                gen_name (str): Имя блока генов ('metabolic', 'move_logic', 'reproduction' и т.д.).

            Returns:
                np.ndarray: Массив значений генов указанного блока.
            """
        return np.array([value for value in self.genes[gen_name].values()], dtype=np.float32)

    def from_array_gen(self, arr: np.array, gen_name: str):
        """
            Обновляет выбранный блок генов из numpy-массива.

            Порядок значений в массиве соответствует порядку ключей словаря блока.

            Args:
                arr (np.ndarray): Массив значений для обновления блока.
                gen_name (str): Имя блока генов, который нужно обновить.
            """
        new = dict(zip(self.genes[gen_name].keys(), arr))
        self.genes[gen_name] = new

    def get_tree_and_root(self, tree, root):
        """
            Сохраняет ссылку на дерево поведения и корень для текущего экземпляра.

            Args:
                tree: Список или структура дерева поведения.
                root: Корневой элемент дерева поведения.
            """
        self.tree = tree
        self.root = root

    def __del__(self):
        print('smert gen')
