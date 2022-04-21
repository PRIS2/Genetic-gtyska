import random
from population import Individual
from typing import TypeVar

G = TypeVar('G')


class Mutation:
    def __init__(self, individual: Individual, mutation_probability: float) -> None:
        self.individual: Individual = individual
        self.probability: float = mutation_probability

    def __next_gene_index(self, gene_index: int) -> int:
        if gene_index >= self.individual.genotype_length:
            gene_index = 0
        else:
            gene_index += 1
        return gene_index

    #swap mutation
    def mutate(self) -> None:
        for i in range(self.individual.genotype_length):
            random_prob: float = random.random()
            if random_prob <= self.probability:
                temp: G = self.individual.genotype[i]
                next_gene_index: int = self.__next_gene_index(i)
                self.individual.genotype[i] = self.individual.genotype[next_gene_index]
                self.individual.genotype[next_gene_index] = temp
