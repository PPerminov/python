from os import *
import nums
from random import *

def simple_for_module(module,res,num=2):
    result=[]
    while len(result) < num:
        position=randrange(2,5478)
        list1=nums.simple(position,9)
        for pos in list1:
            if len(result) >= num:
                break
            elif pos % module == res:
                result.append(pos)
    return result

def dectobin123(number):
    result=""
    while number > 0:
        de = int(number) % 2
        # print(de)
        result = str(de) + str(result)
        number=(number - (number %2))/2
    while len(result) % 8 != 0:
        result="0"+result
    return result




def bit_odd(number):
    if dectobin123(number)[-1] == "0":
        print("Not Odd")
        return
    print("Odd")


bit_odd(7)


# for i in range (1,257):
#     print(dectobin11(i))
#
#
# print(nums.simple(800,2))
