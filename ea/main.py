from ea.algorithm import Algorithm
from ea.problem import Problem
import matplotlib.pyplot

problem = Problem(10, -.1, -.1, 1000)
problem.load_file('../data_20000_0_10.in')
algorithm = Algorithm(problem)

iterations = 50
best_individuals = [0] * iterations

for _ in range(iterations):
    algorithm.iterate()
    result = algorithm.population.individuals
    best_individuals[_] = max(result, key=lambda x: x.fitness(problem)).fitness(problem)


matplotlib.pyplot.plot(range(iterations), best_individuals)
matplotlib.pyplot.show()
