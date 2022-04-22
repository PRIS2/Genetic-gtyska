from individual import Individual
from population import Population
from typing import List


def __print_population(population: Population):
    print('Population:')
    for i in range(population.population_length):
        print(population.individuals_list[i].genotype)


def mutation_test():
    genotype = [1, 2, 3, 4]
    individual = Individual(genotype=genotype)
    print('\nGenotype before mutation')
    print(individual.genotype)
    individual.mutate(mutation_probability=0.7)
    print('\nGenotype after mutation')
    print(individual.genotype)


def crossover_test():
    individuals_list: List[Individual] = []
    for i in range(1, 5):
        genotype: List[int] = [i] * 4
        individual = Individual(genotype=genotype)
        individuals_list.append(individual)

    population = Population(individuals_list=individuals_list)
    print('\nBefore crossover')
    __print_population(population=population)
    population.cross(crossover_probability=0.7)
    print('\nAfter crossover')
    __print_population(population=population)


if __name__ == '__main__':
    mutation_test()
    crossover_test()
