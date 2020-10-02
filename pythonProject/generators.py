import random, itertools

cube_game = (random.randint(1, 6) for i in range(4))

total = 0
for num in cube_game:
    total += num

# permutation
for permutation in itertools.permutations([0, 5, 6, 9]):
    print(permutation)

with open("capitals.txt") as file:
    single_line_gen = (line for line in file)
    capitals_and_cities = \
        (l.replace("\n", " ").split(",") for l in single_line_gen)
    capitals_dict = dict(capitals_and_cities)
    print(capitals_dict["Israel"])


def my_gen(x, y):
    x += 1
    while x < y:
        yield x
        x += 1


for i in my_gen(6, 10):
    print(i)
