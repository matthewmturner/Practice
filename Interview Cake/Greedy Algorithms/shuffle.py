from random import randint


def shuffle(values):

    length = len(values)
    new_list = [None] * length
    used_indices = set()

    for val in values:
        index = randint(0, length - 1)
        while index in used_indices:
            index = randint(0, length - 1)
        new_list[index] = val
        used_indices.add(index)

    for i, val in enumerate(new_list):
        values[i] = val


abc = [1, 2, 3, 4, 5]
shuffle(abc)
print(abc)
