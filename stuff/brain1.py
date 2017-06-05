import ast
from z3 import *

def check_eq(liist):
    tmplist = []
    for unit in liist:
        if unit in tmplist:
            return False
        else:
            tmplist.append(unit)
    return True


list1 = [1, 2, 3, 4, 5, 6]
list2 = [1, 2, 5, 7, 2, 7]
