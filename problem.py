class Problem:
    def __init__(self, value_coefficient, weight_penalty, count_penalty, population_size):
        self.value_coefficient = value_coefficient
        self.weight_penalty = weight_penalty
        self.count_penalty = count_penalty
        self.population_size = population_size

        self.weights = []
        self.max_weight = 0
        self.values = []
        self.individual_size = 0
        self.minimum_objects = 0
        self.maximum_objects = 0

    def load_file(self, filename):
        with open(filename, 'r') as file:
            self.max_weight = int(file.readline())
            self.minimum_objects = int(file.readline())
            self.maximum_objects = int(file.readline())
            self.individual_size = int(file.readline())

            self.weights = list(map(int, file.readline().split(' ')))
            self.values = list(map(int, file.readline().split(' ')))