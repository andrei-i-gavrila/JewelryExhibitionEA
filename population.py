import random

from individual import Individual


class Population:

    def __init__(self, population_size, individual_size, individuals = None):
        if individuals is None:
            individuals = [Individual(individual_size) for _ in range(population_size)]
        self.individuals = individuals
        self.population_size = population_size
        self.individual_size = individual_size

    def new_population(self, problem):
        fitness = [individual.fitness(problem) for individual in self.individuals]

        return Population(
            self.population_size,
            self.individual_size,
            [Individual.crossover(*(random.choices(self.individuals, fitness, None, 2))) for _ in
             range(self.population_size)]
        )
