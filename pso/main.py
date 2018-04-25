import matplotlib.pyplot

from pso.problem import Problem
from pso.swarm import Swarm

problem = Problem(10, -.1, -.1, 100, 100, 1.0, 1.5, 1.0)

problem.load_file('../data_20000_0_10.in')

iterations = 500
swarm = Swarm(problem)

best_individuals = [swarm.iterate_and_get_best(iteration) for iteration in range(iterations)]
matplotlib.pyplot.plot(range(iterations), list(map(lambda i: i.fitness, best_individuals)))
matplotlib.pyplot.show()
