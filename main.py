from algorithm import Algorithm
from problem import Problem
import matplotlib.pyplot

problem = Problem(10, -.1, -.1, 100)
problem.load_file('data_20000_0_40.in')
algorithm = Algorithm(problem)

iterations = 1000
best_individuals = [0] * iterations

for _ in range(1000):
    algorithm.iterate()
    result = algorithm.population.individuals
    sorted_result = sorted(result, key=lambda x: x.fitness(problem), reverse=True)

    best_individuals[_] = sorted_result[0].fitness(problem)


matplotlib.pyplot.plot(range(iterations), best_individuals)
matplotlib.pyplot.show()
