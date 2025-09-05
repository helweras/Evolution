from Creature_components.Genes import Genes
import numpy as np

class Mutator:
    @staticmethod
    def mutate_all(genes, prob: float = 0.1, scale: float = 1.0):
        """
        Применяет векторную мутацию ко всем параметрам генов.

        Args:
            genes: объект Genes
            prob (float): вероятность мутации каждого параметра
            scale (float): максимальное абсолютное изменение параметра

        Returns:
            Genes: новый объект Genes с мутированными параметрами
        """
        # исходный массив всех параметров
        gene_array = genes.to_array_all()

        # создаем массив мутаций той же формы
        mutation_array = np.where(
            np.random.rand(len(gene_array)) < prob,
            np.random.uniform(-scale, scale, size=len(gene_array)),
            0
        )

        # применяем мутации векторно
        new_array = gene_array + mutation_array

        # создаем новый объект Genes и обновляем параметры
        new_genes = Genes()
        new_genes.from_array_all(new_array)
        return new_genes

    @staticmethod
    def mutate_block(genes, block_name: str, prob: float = 0.1, scale: float = 1.0):
        """
        Применяет мутацию только к одному блоку генов.

        Args:
            genes: объект Genes
            block_name (str): имя блока ('metabolic', 'move_logic', 'reproduction' и т.д.)
            prob (float): вероятность мутации каждого параметра блока
            scale (float): максимальное абсолютное изменение параметра

        Returns:
            Genes: новый объект Genes с мутированным блоком
        """
        # исходный массив параметров блока
        gene_block = genes.to_array_gen(block_name)

        # массив мутаций той же формы
        mutation_block = np.where(
            np.random.rand(len(gene_block)) < prob,
            np.random.uniform(-scale, scale, size=len(gene_block)),
            0
        )

        # применяем мутации векторно
        new_block = gene_block + mutation_block

        # создаем новый объект Genes и обновляем блок
        new_genes = Genes()
        # сначала копируем остальные блоки
        for b in genes.genes:
            if b != block_name:
                new_genes.genes[b] = genes.genes[b].copy()
        # обновляем мутированный блок
        new_genes.from_array_gen(new_block, block_name)

        return new_genes





