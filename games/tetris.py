cube = [[1, 1], [1, 1]]
stick = [[1, 1, 1, 1]]
leftHorse = [[0, 0, 0, 1], [1, 1, 1, 1]]
rightHorse = [[1, 1, 1, 1], [0, 0, 0, 1]]
leftZ = [[1, 1, 0], [0, 1, 1]]
rightZ = [[0, 1, 1], [1, 1, 0]]
triple = [[1, 1, 1], [0, 1, 0]]


def matrix_size(matrix):
    return [len(matrix), len(matrix[0])]


def rotateLeft(figure):
    size = matrix_size(figure)
    newRows = size[1]
    newCols = size[0]
    newFigure = []
    counter = 0
    for row in range(0, newRows):
        newFigure.append([])
        for col in range(0, newCols):
            counter += 1
            newFigureSize = len(newFigure) - 1
            newFigure[newFigureSize].append(figure[col][newRows - row - 1])

    return newFigure


def rotateRight(figure):
    size = matrix_size(figure)
    newRows = size[1]
    newCols = size[0]
    newFigure = []
    counter = 0
    for row in range(0, newRows):
        newFigure.append([])
        for col in range(0, newCols):
            counter += 1
            newFigureSize = len(newFigure) - 1
            newFigure[newFigureSize].append(figure[newCols - col - 1][row])

    return newFigure


def dropFullLines(field):
    length = len(field)
    positionsInLine = len(field[0])
    additionalLine = []
    while len(additionalLine) != positionsInLine:
        additionalLine.append(0)

    def worker(accum, position, counter):
        if position == length:
            return accum
        currentLine = field[position]
        print accum
        if sum(currentLine) == positionsInLine:
            return worker(accum, position + 1, counter + 1)
        accum.append(currentLine)
        return worker(accum, position + 1)
    newField = worker([], 0)
    while len(newField) < length:
        newField.append(additionalLine)
    return newField[::-1]


field = [[1, 1, 1, 1], [1, 1, 1, 1], [1, 0, 1, 1],
         [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]

print(dropFullLines(field))
