from itertools import permutations

def possible_permutations(list_nums):
    for el in permutations(list_nums):
        yield list(el)


[print(n) for n in possible_permutations([1, 2, 3])]

