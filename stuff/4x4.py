from sys import *
import math
# import string
a1 = [0, 1, 2, 3]
a2 = [4, 5, 6, 7]
a3 = [8, 9, 10, None]
a4 = [12, 13, 14, 11]
a = [a1, a2, a3, a4]
b1 = [0, 4, 5]
b2 = [2, 1, 3]
b3 = [7, 6, None]
b = [b1, b2, b3]


def check_field(field):
    for row in range(1, len(field)):
        if len(field[row]) != len(field[row - 1]):
            return False
    return True


def move_up(field, row, col):
    if field[row - 1][col] != None:
        return False
    tmp = field[row][col]
    field[row][col] = None
    field[row - 1][col] = tmp
    return field


def move_down(field, row, col):
    try:
        field[row + 1][col]
    except IndexError:
        print("HolyShit")
    else:
        if field[row + 1][col] != None:
            return False
        tmp = field[row][col]
        field[row][col] = None
        field[row + 1][col] = tmp
        return field


def move_left(field, row, col):
    try:
        field[row][col - 1]
    except IndexError:
        print("HolyShit")
    else:
        if field[row][col - 1] != None:
            return False
        tmp = field[row][col]
        field[row][col] = None
        field[row][col - 1] = tmp
        return field


def move_right(field, row, col):
    try:
        field[row][col + 1]
    except IndexError:
        print("HolyShit")
    else:
        if field[row][col + 1] != None:
            return False
        tmp = field[row][col]
        field[row][col] = None
        field[row][col + 1] = tmp
        return field


def import_from_file(filename):
    strings = []
    with open(filename) as file:
        raw = file.readlines()
    rows = len(raw)
    for line in raw:
        strings.append(line.split())
    return strings


def indexer(field):  # here I need to index field for numbers positions and None position
    in_dream = {}
    in_fact = {}
    counter = 0
    number = (len(field) * len(field[0])) # всего полей
    for row in range(len(field)):
        for column in range(len(field[row])):
            in_dream[counter] = [row, column]
            cur = field[row][column]
            in_fact[cur] = [row, column]
            counter += 1
    print (len(in_fact), len(in_dream))
    for i in range(number):
        print('index %s now in position %tx%y. It must be on position %ux%i. %o turns', [
              i, in_fact[i][0], in_fact[i][1], in_dream[i][0], in_dream[i][1], abs((in_fact[i][0] + in_fact[i][1]) - (in_dream[i][0] + in_dream[i][1]))])

def getPosition(cube,field):
    for row in range(len(field)):
        for column in range(len(field[row])):
            if(field[row][column] == cube):
                return [row,column]
            continue;

def getEthalonPosition(cube,rows = 4, columns = 4):
    return [math.floor(cube / rows) - 1, (cube % columns)]


# print(import_from_file('4.txt'))
# indexer(b)
# print(getPosition(3,b))
#
# print(getEthalonPosition(8))

def getMovesNumber(currentPosition,futherPosition):
    a=abs(currentPosition[0] - futherPosition[0])
    b=abs(currentPosition[1] - futherPosition[1])
    return a + b

def checkNone(position,field,turn=0):
    row=position[0]
    column=position[1]
    s1='none'
    if (turn == 4):
        return False
    elif (turn == 0):
        try:
            none = field[row][column+1]
        finally:
            if none == 'none':
                return [row,column+1]
    elif (turn == 1):
        try:
            none = field[row][column-1]
        fsinally:
            if none == 'none':
                return [row,column-1]
    elif (turn == 2):
        try:
            none = field[row+1][column]
        finally:
            if none == 'none':
                return [row+1,column]
    elif (turn == 3):
        try:
            none = field[row-1][column]
        finally:
            if none == 'none':
                return [row+1,column]
    else:
        return checkNone(position,field,turn+1)


print(checkNone([1,3],a))
# def getMovings(currentPosition,futherPosition):
