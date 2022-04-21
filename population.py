from typing import TypeVar, List

G = TypeVar('G')


class Individual:
    def __init__(self, genotype: List[G]):
        self.genotype = genotype
        self.genotype_length = len(genotype)


class Population:
    def __init__(self, population: List[Individual]):
        self.population = population
        self.population_length = len(population)
