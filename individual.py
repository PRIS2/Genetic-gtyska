from typing import TypeVar, List
import random
from utils import get_next_index

G = TypeVar('G')


class Individual:
    def __init__(self, genotype: List[G]) -> None:
        """Inits Individual class with list of genes."""
        self.genotype = genotype
        self.genotype_length = len(genotype)

    def mutate(self, mutation_probability: float) -> None:
        for i in range(self.genotype_length):
            random_prob: float = random.random()
            if random_prob <= mutation_probability:
                temp: G = self.genotype[i]
                next_gene_index: int = get_next_index(i, self.genotype_length)
                self.genotype[i] = self.genotype[next_gene_index]
                self.genotype[next_gene_index] = temp
