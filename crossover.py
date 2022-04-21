from population import Individual


class Crossover:
    def __init__(self, individual_1: Individual, individual_2: Individual):
        self.individual_1: Individual = individual_1
        self.individual_2: Individual = individual_2
