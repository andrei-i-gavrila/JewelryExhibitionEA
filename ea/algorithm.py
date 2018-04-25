from ea.population import Population


class Algorithm:

    def __init__(self, problem):
        self.problem = problem
        self.population = Population(problem.population_size, problem.individual_size)

    def iterate(self):
        self.population = self.population.new_population(self.problem)
