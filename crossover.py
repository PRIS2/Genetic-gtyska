from individual import Individual
import random
from typing import TypeVar, List

G = TypeVar('G')


class Crossover:
    def __init__(self, individual_1: Individual, individual_2: Individual):
        self.individual_1: Individual = individual_1
        self.individual_2: Individual = individual_2

    def run(self) -> None:
        genotype_length: int = self.individual_1.genotype_length
        gene_index_start: int = random.randint(1, genotype_length - 1)
        ind_1_genotype_copy: List[G] = self.individual_1.genotype.copy()
        ind_2_genotype_copy: List[G] = self.individual_2.genotype.copy()
        self.individual_1.genotype = ind_1_genotype_copy[0:gene_index_start] + \
                                     ind_2_genotype_copy[gene_index_start:genotype_length]
        self.individual_2.genotype = ind_2_genotype_copy[0:gene_index_start] + \
                                     ind_1_genotype_copy[gene_index_start:genotype_length]
