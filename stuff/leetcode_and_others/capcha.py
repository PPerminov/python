from capcha_data import *
from sys import setrecursionlimit
setrecursionlimit(2000)
##import time

# t=time.time()
# sum1=0
# prev=capcha[-1]

# length=len(capcha)

# for cap in range(length):
# if capcha[cap] == prev:
# sum1+=int(capcha[cap])
# prev=capcha[cap]

##print("Capcha 1",sum1)

##print(time.time() -t)



# def initer(ar):
# ret=[]
# ar=ar.split('\t')
# for item in ar:
# ret.append(int(item))
# return ret


# data=data.split('\n')
# data=list(map(initer,data))
# print(data)


# checksum=0
# for line in data:
# mi=min(line)
# ma=max(line)
# dif=ma-mi
# print(dif)
# checksum+=dif
# print("Checksum:",checksum)

# array=0

# for line in data:

# for item in line:
# for i in line:
# if item != i and item % i == 0 :
##array+=int(item / i)

# print(array)


# def steps(step):
#from math import sqrt
# level_fl=sqrt(step)
# level=int(level_fl)
# steps=0
# if level % 2 == 0:
# level+=1
# elif (level_fl > level):
# level+=2
# for _ in range(1,level,2):
# steps+=1
# print(steps)
#prevlevel=level - 2
# start=(prevlevel*prevlevel)
# end=level*level
#side_size=(end - start)/4
# for i in range(1,5):
#cur_end = start + side_size
# print(cur_end)
# if step == cur_end:
#position = cur_end
# break
# if  step < cur_end and step >= start :
# side=i
# count_start=start
# count_end=cur_end
# middle=int((count_start+count_end)/2)
#position_added=abs(middle - step)
# start=cur_end
# return (steps + position_added)
# print(steps(289326))


# def spiral_build(number,array=[[1,1]],position=(0,0)):
# def up(array,size, position, point):
# array.insert(0,[point])
# return array
# def down(array,size, position, point, pos=0,temp=[]):
# if pos == size:
# array.insert(len(array),temp)
# return array
# if pos == position:
# temp.append(position)
# return down(array,size, position, point, pos+1,temp)
# temp.append(0)
# return down(array,size, position, point, pos+1,temp)
# def left(array,row,point):
# array[row].insert(0,point)
# def right(array,row,point):
# array[row].insert(len(array[row],point))
# def mapper(num,array):
# current=count(array[0])
# x=count(array[0])
# y=count(array)

# while True:
# if not array[y][x]

# def get_surrounders(array,position):
# x=position[0]
# y=position[1]
# surrounders=[]
# positions=((x-1,y),
# (x+1,y),
# (x-1,y-1),
# (x,y-1),
# (x+1,y-1),
# (x-1,y+1),
# (x,y+1),
# (x+1,y+1))
# for position in positions:
# x=position[0]
# y=position[1]
# print(x,y)
# if x < 0 or y < 0:
# continue
# try:
# current=array[x][y]
# surrounders.append(current)
# except:
# continue
# return surrounders

# if not array[row-1]:
# array=up(array,)





# def down(array,size, position, point, pos=0,temp=[]):
# if pos == size:
# array.insert(len(array),temp)
# return array
# if pos == position:
# temp.append(point)
# return down(array,size, position, point, pos+1,temp)
# temp.append(0)
# return down(array,size, position, point, pos+1,temp)

# def right(array,position, point, pos=0):
# for i in range(len(array)):
# if i == position:
# array[i].append(point)
# else:
# array[i].append(0)
# return array

# def mkarray(size):
# array=[]
# while size >0 :
# array.append(0)
# size-=1
# return array

# def get_surrounders(array,position):
# x=position[0]
# y=position[1]
# surrounders=[]
# positions=((x-1,y),
#(x+1,y),
#(x-1,y-1),
#(x,y-1),
#(x+1,y-1),
#(x-1,y+1),
#(x,y+1),
#(x+1,y+1))
# for position in positions:
# x=position[0]
# y=position[1]
# print(x,y)
# if x < 0 or y < 0:
# continue
# try:
# current=array[x][y]
# surrounders.append(current)
# except:
# continue
# return sum(surrounders)

# def add_circle(array):
# for item in drama:
# print(item)
#import math
# cur=len(array[0])
# if len(array[0]) -1 != cur:
# return False
# last_point=array[len(array)-1][len(array[0])-1]
#new = cur
# new_line1=mkarray(new+2)
# new_line0=mkarray(new+2)
# for i in range(len(array)):
# array[i].insert(0,0)
# array[i].insert(len(array[i]),0)
# array.insert(0,new_line1)
# array.append(new_line0)
# rows=len(array)-1
# cols=len(array[0])-1
# row=rows-1
# col=cols
# iters=0
# while True:
# iters+=1
# print(col,cols,row)
# last_point+=1
# print(last_point)
# if row == rows and col == cols:
# array[row][col]=get_surrounders(array,[row,col])
# break
# if col == cols and row !=0:
# array[row][col]=get_surrounders(array,[row,col])
# array[row][col]=last_point
# row-=1
# continue
# if col == cols and row == 0:
# array[row][col]=last_point
# array[row][col]=get_surrounders(array,[row,col])
# col-=1
# continue
# if row==0 and col !=0:
# array[row][col]=last_point
# array[row][col]=get_surrounders(array,[row,col])
# col-=1
# continue
# if row==0 and col ==0:
# array[row][col]=last_point
# array[row][col]=get_surrounders(array,[row,col])
# row+=1
# continue
# if row != rows and col == 0:
# array[row][col]=last_point
# array[row][col]=get_surrounders(array,[row,col])
# row+=1
# continue
# if row == rows and col == 0:
# array[row][col]=last_point
# array[row][col]=get_surrounders(array,[row,col])
# col+=1
# continue
# if row == rows and col != cols:
# array[row][col]=get_surrounders(array,[row,col])
# array[row][col]=last_point
# col+=1
# continue

# if x ==

##whole_line=list(range(last_point + 1, int(pow(math.sqrt(last_point) + 2,2)) + 1 ))
# denom=2
# while True:
##y=len(array) -  denom
# x=
# last_point+=1
# array[y][x]=last_point
# print(iters)
# return array
# print(last_point)


# print(add_circle(drama))
# def check(array):
# for item in array:
# item.sort()
# for item1 in item:
# if item1 > 289326:
# print(item1)
# return True

# ar=[[1]]

# while True:
# ar=add_circle(ar)
# if check(ar):
# break
# for item in ar:
#print( item)
# print('---')

# for i in ar:
# print(i)

# ar[2][12]=65454851
# print(ar)


# day 4


# data=input1.split('\n')
# data = list(d.split(' ') for d in input1.split('\n'))
# app = []
# for item in data:
#     l1 = len(item)
#     item1 = set(item)
#     if len(item1) == l1:
#         app.append(item)
#
# ar1=[]
# appr=0
# for item in app:
#     new_line=[]
#     for word in item:
#         word1=list(word)
#         word1.sort()
#         word=''.join(word1)
#         if not word in new_line:
#             new_line.append(''.join(word))
#     if len(new_line) == len(item):
#         appr+=1
#
# print(appr)


# day 5
# day5 = list(map(lambda x: int(x), day5_raw.split('\n')))
#
#
# def jumps(data):
#     position = 0
#     jump = 0
#     while True:
#         if position < 0:
#             return jump

# day 6
# from zlib import crc32
#
# data = day6_raw
#
#
# def infi_loop(data, results=[]):
#     def maximus():
#         current_max = 0
#         current_position =0
#         for i in range(len(data)):
#             if data[i] > current_max:
#                 current_max = data[i]
#                 current_position = i
#         return current_position
#
#
#     def iterator(position,summ):
#         if summ == 0:
#             return
#         if position == len(data):
#             position = 0
#         summ -= 1
#         data[position] += 1
#         position += 1
#         return iterator(position, summ)
#     a=0
#     checksums=[]
#     while True:
#         current_position=maximus()
#         a += 1
#         summ=data[current_position]
#         data[current_position]=0
#         iterator(current_position+1,summ)
#
#         current_checksumm =crc32(('/'.join(list(map(lambda x: str(x),data)))).encode())
#         if not current_checksumm in checksums:
#             checksums.append(current_checksumm)
#         else:
#             return a
#
#
# def infi_loop1(data, results=[]):
#     start=crc32(('/'.join(list(map(lambda x: str(x),data)))).encode())
#     def maximus():
#         current_max = 0
#         current_position =0
#         for i in range(len(data)):
#             if data[i] > current_max:
#                 current_max = data[i]
#                 current_position = i
#         return current_position
#
#     current_checksumm=0
#     def iterator(position,summ):
#         if summ == 0:
#             return
#         if position == len(data):
#             position = 0
#         summ -= 1
#         data[position] += 1
#         position += 1
#         return iterator(position, summ)
#     a=0
#     checksums=[]
#     while current_checksumm != start:
#         current_position=maximus()
#         a += 1
#         summ=data[current_position]
#         data[current_position]=0
#         iterator(current_position+1,summ)
#
#         current_checksumm =crc32(('/'.join(list(map(lambda x: str(x),data)))).encode())
#         # if not current_checksumm in checksums:
#         #     checksums.append(current_checksumm)
#         # else:
#     return a
#
# print(infi_loop(data))
# print(infi_loop1(data))
