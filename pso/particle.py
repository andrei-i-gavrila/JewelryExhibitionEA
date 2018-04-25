from math import exp
from random import random

from numpy.ma import dot, subtract

from pso.problem import Problem


class Particle:

    def __init__(self, id, problem: Problem):
        self.id = id
        self.problem = problem
        self.velocity = [0] * self.problem.individual_size
        self.position = [round(random()) for _ in range(self.problem.individual_size)]
        self.best_position = self.position
        self.fitness = self.evaluate()
        self.best_fitness = self.fitness
        self.neighbourhood = []

    def evaluate(self):
        total_value = dot(self.problem.values, self.position)
        total_weight = dot(self.problem.weights, self.position)

        fitness = total_value * self.problem.value_coefficient

        if total_weight > self.problem.max_weight:
            fitness += (total_weight - self.problem.max_weight) * self.problem.weight_penalty

        elements_count = sum(self.position)
        if elements_count > self.problem.maximum_objects:
            fitness += (elements_count - self.problem.maximum_objects) * self.problem.count_penalty
        if elements_count < self.problem.minimum_objects:
            fitness += (self.problem.maximum_objects - elements_count) * self.problem.count_penalty

        return fitness

    def update(self, position):
        self.position, self.fitness = position, self.evaluate()
        if self.fitness > self.best_fitness:
            self.best_fitness, self.best_position = self.fitness, self.position

    def best_neighbour(self):
        return max(self.neighbourhood, key=lambda p: p.best_fitness)

    def iterate(self, inertia):
        best_neighbour = self.best_neighbour()
        if best_neighbour.id == self.id:
            return
        best_neighbour_position = best_neighbour.position

        self.velocity = [inertia * v for v in self.velocity]
        random_vec = [self.problem.local_coeff * random() for _ in range(self.problem.individual_size)]
        self.velocity += random_vec * subtract(self.best_position, self.position)
        random_vec = [self.problem.global_coeff * random() for _ in range(self.problem.individual_size)]
        self.velocity += random_vec * subtract(best_neighbour_position, self.position)

        new_position = [1 if random() < 1 / (1 + exp(-v)) else 0 for v in self.velocity]
        new_position = [self.position[i] if self.velocity[i] == 0 else new_position[i] for i in
                        range(self.problem.individual_size)]
        self.update(new_position)

    def iterate_get_fitness(self, inertia):
        self.iterate(inertia)
        return self.fitness
