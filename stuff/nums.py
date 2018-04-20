# How to find siple numbers?


def simple(num, colvo):
    if num % 2 == 0:  # first of all We must use only odd numbers and begins with odd
        num += 1
    delimiter = 3  # delimiter for search. It musn't be less than 3.
    list1 = []  # list for results
    while len(list1) < colvo:  # While we not get all numbers :)
        # if we increase delimiter to level of num/3 (that means that num is a simple)
        if delimiter >= num / 3:
            list1 += [num]  # then add this number to list
            delimiter = 3  # get delimiter to default 3
            num += 2  # increase number by 2
            continue
        if num % delimiter == 0:  # if some of delimiters are divide num without residue
            delimiter = 3  # reset all
            num += 2
            continue
        delimiter += 2  # inrease delimiter
    return list1

# usage:
# simple(number for beginning of search, num of simples to find)
# print(simple(3,10))
