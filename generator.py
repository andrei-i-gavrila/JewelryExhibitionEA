from math import floor
from random import randint, random


def get_file_name(max_weight: int, min_objects: int, max_objects: int):
    return 'data_' + '_'.join(map(str, [max_weight, min_objects, max_objects])) + '.in'


def generate(max_weight: int, minimum_objects: int, maximum_objects: int):
    filename = get_file_name(max_weight, minimum_objects, maximum_objects)
    with open(filename, 'w') as file:
        file.write(str(max_weight) + '\n')
        file.write(str(minimum_objects) + '\n')
        file.write(str(maximum_objects) + '\n')

        item_count = randint(minimum_objects, floor((1 + random()) * maximum_objects))

        file.write(str(item_count) + '\n')

        item_weights = (randint(0, max_weight) for _ in range(item_count))
        item_values = (randint(0, 1000) for _ in range(item_count))

        file.write(' '.join(map(str, item_weights)) + '\n')
        file.write(' '.join(map(str, item_values)) + '\n')


generate(20000, 100, 200)
