from random import randint
from time import time


def uniq_clasic(some, g=[]):
    for i in some:
        if i not in g:
            g.append(i)
    return g


def uniq_enumerate(source):
    return [item for i, item in enumerate(source) if item not in source[0:i]]


def uniq_dst(source):
    dst = []
    [dst.append(item) for item in source if item not in dst]
    return dst


def uniq_source(source):
    [source.pop(i) for i in range(len(source))[::-1]
     if source.count(source[i]) > 1]
    return source


def uniq_set(source):
    return list(set(source))


count = 1000000

original = []
time1 = time()
print('Generating...')
for i in range(count):
    original.append(randint(0, count))
time2 = time()
print('Enumerating...')
enumer = uniq_enumerate(original)
time3 = time()
print('DSTing....')
dst = uniq_dst(original)
time4 = time()
print('Sourcing...')
source = uniq_source(original)
time5 = time()
print('SETTING....')
set1 = uniq_set(original)
time6 = time()
print('Classic...')
classic = uniq_clasic(original)
time7 = time()

dict1 = {}

# dict1['Original time']=time2 - time1
dict1['Enumerate time'] = time3 - time2
dict1['DST time'] = time4 - time3
dict1['SOURCE time'] = time5 - time4
dict1['SET time'] = time6 - time5
dict1['Classic time'] = time7 - time6

# def sort1(dict1):
#     for i,k in dict1.items():


print(dict1)


#
# print(enumer)
# print(dst)
# print(source)
# print(set1)
