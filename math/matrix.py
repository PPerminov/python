from math import *
from random import *
# from functools import reduce
# from goto import goto,label

matrix1=[[3,1],[-3,1]]
#matrix1='a'
# matrix2=[[3,1],[-3,4]]
# matrix2="sdgfsdfs"
matrix2=[[3,1],[6,1],[6,1]]

def is_matrix(matrix,verbose=0):
    result=[]
    if type(matrix) != list:
        result.append(0)
    rowpos=0
    columns_from_source=matrix_size(matrix)[1]
    columns_in_fact=0
    for row in matrix:
        colpos=0
        columns_in_fact=len(row)
        if type(row) != list:
            result.append(1)
        for col in row:
            try:
                col+1
            except:
                result.append(2)
            colpos+=1
        rowpos+=1
    if (columns_in_fact != columns_from_source):
        result.append(3)
    if result != []:
        if verbose!=0:
            for item in result:
                if item == 0:
                    print("Bad argument\nIt (they) must be list(s)")
                    return False
                elif item == 1:
                    print("Bad argument\nAny part of argument must be list")
                    # print("Bad position is " + str(rowpos) + ":" + str(colpos))
                    return False
                elif item == 2:
                    print("Bad argument\nSome matrix data is not numbers?")
                    # print("Bad position is " + str(rowpos) + ":" + str(colpos))
                    return False
                elif item == 3:
                    print("Bad argument\nRows are not equal")
                    # print("Bad position is " + str(rowpos) + ":" + str(colpos))
                    return False
        return False
    else:
        return True



def matrix_size(matrix):
    return [len(matrix),len(matrix[0])]

def matrix_generate(rows,cols):
    new_matrix=[]
    for row in range(0,rows,1):
        new_matrix.append(list())
        for col in range(0,cols,1):
            new_matrix[row].append(randrange(10))
    return new_matrix

def matrix_get_position(matrix,row,col):
    return matrix[row][col]

def matrix_transpose(matrix):
    size=matrix_size(matrix)
    rows=size[0]          #new cols. All new cols must be = rows. We will need to count
    cols=size[1]          #new rows. All new rows must be = cols.
    new_matrix=[]         #new matrix will
    tmp_count=0
    for row in range(0,cols,1):
        new_matrix.append(list())
        for col in range(0,rows,1):
            new_matrix[row].append(matrix_get_position(matrix,col,row))
    return new_matrix

def matrix_sum(matrix1,matrix2):
    new_matrix=[]
    for row in range(0,matrix_size(matrix1)[0],1):
        new_matrix.append([])
        for col in range(0,matrix_size(matrix1)[1],1):
            new_matrix[row].append(matrix1[row][col]+matrix2[row][col])
    return new_matrix

def matrix_multiply(matrix1,matrix2):
    """
    Usage:
    matrix_multiply(matrix1,matrix2)
    matrix2 can be a number to moltiply matrix1 with it
    """
    new_matrix=[]
    if (not is_matrix(matrix1)):
        print('Bad matrix1')
        return False
    elif (type(matrix2) != int):
        if not (is_matrix(matrix2)):
            print('Bad matrix2')
            return False
    if type(matrix2) == int:
        for row in range(0,matrix_size(matrix1)[0],1):
            new_matrix.append([])
            for col in range(0,matrix_size(matrix1)[1],1):
                new_matrix.append(matrix_get_position(matrix1,row,col)*matrix2)
        return new_matrix
    matrix1_size=matrix_size(matrix1)
    matrix2_size=matrix_size(matrix2)
    if matrix1_size[1] != matrix2_size[0]:
        print('Bad matrix size')
        return False
    new_matrix_size=[matrix1_size[0],matrix2_size[1]]
    matrix2=matrix_transpose(matrix2)
    for row in range(0,new_matrix_size[0],1):
        new_matrix.append([])
        for col in range(0,new_matrix_size[1],1):
            value=0
            for position in range(0,new_matrix_size[0],1):
                value+=matrix_get_position(matrix1,row,position)*matrix_get_position(matrix2,col,position)
            new_matrix[row].append(value)
    return new_matrix

print(matrix_multiply(matrix1,6))
