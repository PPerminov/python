from random import randint


def randomABC():
    a = randint(1, 5464)
    b = randint(1, 5464)
    c = randint(1, 5464)
    return [a, b, c]


def find_solution():
    counter = 0
    numbers = randomABC()
    while (numbers[0] * numbers[1] != numbers[2]):
        numbers = randomABC()
        counter += 1
    return counter


array = []
while len(array) <= 1000:
    array.append(find_solution())

print(min(array))
print(max(array))
