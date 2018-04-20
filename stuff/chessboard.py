import sys

sys.setrecursionlimit(20000)

def chessBoard_loops():
    board = "----------\n"
    for r in range(8):
        line = '|'
        for c in range(8):
            if ((c + r) % 2 == 0):
                line += "x"
            else:
                line += " "
        board += line + "|\n"
    return board + "----------"


def chessBoard_recursion(row=0, col=0, size=8):
    if row == (size - 1) and col == size:
        line=""
        for i in range(size+2):
            line+='-'
        return "\n"+line
    if col == size:
        return "\n" + chessBoard_recursion(row + 1, 0)
    if ((col + row) % 2 == 0):
        current = "x"
    else:
        current = " "
    if col == 0:
        current = '|' + current
    if col == size-1:
        current += '|'
    if row == 0 and col == 0:
        line=""
        for i in range(size+2):
            line+='-'
        current = line + "\n" + current
    return current + chessBoard_recursion(row, col + 1)


print(chessBoard_recursion())
print(chessBoard_loops())
