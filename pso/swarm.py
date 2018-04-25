from random import sample

from pso.particle import Particle
from pso.problem import Problem


class Swarm:

    def __init__(self, problem: Problem):
        self.problem = problem
        self.particles = [Particle(_, self.problem) for _ in range(problem.population_size)]
        self.create_neighbourhoods()

    def create_neighbourhoods(self):
        for particle in self.particles:
            particle.neighbourhood = sample(self.particles, self.problem.neighbourhood_size)

    def iterate_and_get_best(self, iteration):
        best_particle = max(self.particles,
                            key=lambda p: p.iterate_get_fitness(self.problem.initial_inertia))
        # print(best_particle.velocity)
        return best_particle
