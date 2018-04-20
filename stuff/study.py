# import matplotlib.pyplot as plt


def walls(list1):
    # top=0
    tmp=0
    prev=0
    for i in range(1,len(list1)):
        if list1[i-1]<list1[i]:
            print(list1[i])



walls([1,5,8,2,5,6])
