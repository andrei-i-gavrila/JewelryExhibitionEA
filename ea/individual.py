from random import random, randint

from numpy import dot


class Individual:

    def __init__(self, size, data=None):
        self.size = size
        self.data = data if data is not None else [round(random()) for _ in range(self.size)]
        self.fitness_value = None

    def mutate(self, probability: float):
        if probability > random():
            self.data[randint(0, self.size - 1)] = round(random())

    def crossover(self, other, problem):
        return Individual(self.size, [self.data[i] if random() < .5 else other.data[i] for i in range(self.size)])

    def fitness(self, problem):
        if self.fitness_value is not None:
            return self.fitness_value
        total_value = dot(problem.values, self.data)
        total_weight = dot(problem.weights, self.data)

        self.fitness_value = total_value * problem.value_coefficient

        if total_weight > problem.max_weight:
            self.fitness_value += (total_weight - problem.max_weight) * problem.weight_penalty

        elements_count = sum(self.data)
        if elements_count > problem.maximum_objects:
            self.fitness_value += (elements_count - problem.maximum_objects) * problem.count_penalty
        if elements_count < problem.minimum_objects:
            self.fitness_value += (problem.maximum_objects - elements_count) * problem.count_penalty

        # if self.fitness_value < 0:
        #     self.fitness_value = .1

        return self.fitness_value
