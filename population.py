from typing import TypeVar, List
import random
from utils import get_next_index
from crossover import Crossover
from individual import Individual

G = TypeVar('G')


class Population:
    def __init__(self, individuals_list: List[Individual]) -> None:
        self.individuals_list = individuals_list
        self.population_length = len(individuals_list)

    def cross(self, crossover_probability: float) -> None:
        for i in range(self.population_length):
            random_prob: float = random.random()
            if random_prob <= crossover_probability:
                individual_1: Individual= self.individuals_list[i]
                individual_2_index: int = get_next_index(i, self.population_length)
                individual_2: Individual = self.individuals_list[individual_2_index]
                crossover = Crossover(individual_1=individual_1, individual_2=individual_2)
                crossover.run()
