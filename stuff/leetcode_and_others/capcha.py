from capcha_data import *
from functools import reduce
from sys import setrecursionlimit
setrecursionlimit(20000000)
# # ##import time
# #
# # # t=time.time()
# # # sum1=0
# # # prev=capcha[-1]
# #
# # # length=len(capcha)
# #
# # # for cap in range(length):
# # # if capcha[cap] == prev:
# # # sum1+=int(capcha[cap])
# # # prev=capcha[cap]
# #
# # ##print("Capcha 1",sum1)
# #
# # ##print(time.time() -t)
# #
# #
# # # def initer(ar):
# # # ret=[]
# # # ar=ar.split('\t')
# # # for item in ar:
# # # ret.append(int(item))
# # # return ret
# #
# #
# # # data=data.split('\n')
# # # data=list(map(initer,data))
# # # print(data)
# #
# #
# # # checksum=0
# # # for line in data:
# # # mi=min(line)
# # # ma=max(line)
# # # dif=ma-mi
# # # print(dif)
# # # checksum+=dif
# # # print("Checksum:",checksum)
# #
# # # array=0
# #
# # # for line in data:
# #
# # # for item in line:
# # # for i in line:
# # # if item != i and item % i == 0 :
# # ##array+=int(item / i)
# #
# # # print(array)
# #
# #
# # # def steps(step):
# # #from math import sqrt
# # # level_fl=sqrt(step)
# # # level=int(level_fl)
# # # steps=0
# # # if level % 2 == 0:
# # # level+=1
# # # elif (level_fl > level):
# # # level+=2
# # # for _ in range(1,level,2):
# # # steps+=1
# # # print(steps)
# # #prevlevel=level - 2
# # # start=(prevlevel*prevlevel)
# # # end=level*level
# # #side_size=(end - start)/4
# # # for i in range(1,5):
# # #cur_end = start + side_size
# # # print(cur_end)
# # # if step == cur_end:
# # #position = cur_end
# # # break
# # # if  step < cur_end and step >= start :
# # # side=i
# # # count_start=start
# # # count_end=cur_end
# # # middle=int((count_start+count_end)/2)
# # #position_added=abs(middle - step)
# # # start=cur_end
# # # return (steps + position_added)
# # # print(steps(289326))
# #
# #
# # # def spiral_build(number,array=[[1,1]],position=(0,0)):
# # # def up(array,size, position, point):
# # # array.insert(0,[point])
# # # return array
# # # def down(array,size, position, point, pos=0,temp=[]):
# # # if pos == size:
# # # array.insert(len(array),temp)
# # # return array
# # # if pos == position:
# # # temp.append(position)
# # # return down(array,size, position, point, pos+1,temp)
# # # temp.append(0)
# # # return down(array,size, position, point, pos+1,temp)
# # # def left(array,row,point):
# # # array[row].insert(0,point)
# # # def right(array,row,point):
# # # array[row].insert(len(array[row],point))
# # # def mapper(num,array):
# # # current=count(array[0])
# # # x=count(array[0])
# # # y=count(array)
# #
# # # while True:
# # # if not array[y][x]
# #
# # # def get_surrounders(array,position):
# # # x=position[0]
# # # y=position[1]
# # # surrounders=[]
# # # positions=((x-1,y),
# # # (x+1,y),
# # # (x-1,y-1),
# # # (x,y-1),
# # # (x+1,y-1),
# # # (x-1,y+1),
# # # (x,y+1),
# # # (x+1,y+1))
# # # for position in positions:
# # # x=position[0]
# # # y=position[1]
# # # print(x,y)
# # # if x < 0 or y < 0:
# # # continue
# # # try:
# # # current=array[x][y]
# # # surrounders.append(current)
# # # except:
# # # continue
# # # return surrounders
# #
# # # if not array[row-1]:
# # # array=up(array,)
# #
# #
# # # def down(array,size, position, point, pos=0,temp=[]):
# # # if pos == size:
# # # array.insert(len(array),temp)
# # # return array
# # # if pos == position:
# # # temp.append(point)
# # # return down(array,size, position, point, pos+1,temp)
# # # temp.append(0)
# # # return down(array,size, position, point, pos+1,temp)
# #
# # # def right(array,position, point, pos=0):
# # # for i in range(len(array)):
# # # if i == position:
# # # array[i].append(point)
# # # else:
# # # array[i].append(0)
# # # return array
# #
# # # def mkarray(size):
# # # array=[]
# # # while size >0 :
# # # array.append(0)
# # # size-=1
# # # return array
# #
# # # def get_surrounders(array,position):
# # # x=position[0]
# # # y=position[1]
# # # surrounders=[]
# # # positions=((x-1,y),
# # #(x+1,y),
# # #(x-1,y-1),
# # #(x,y-1),
# # #(x+1,y-1),
# # #(x-1,y+1),
# # #(x,y+1),
# # #(x+1,y+1))
# # # for position in positions:
# # # x=position[0]
# # # y=position[1]
# # # print(x,y)
# # # if x < 0 or y < 0:
# # # continue
# # # try:
# # # current=array[x][y]
# # # surrounders.append(current)
# # # except:
# # # continue
# # # return sum(surrounders)
# #
# # # def add_circle(array):
# # # for item in drama:
# # # print(item)
# # #import math
# # # cur=len(array[0])
# # # if len(array[0]) -1 != cur:
# # # return False
# # # last_point=array[len(array)-1][len(array[0])-1]
# # #new = cur
# # # new_line1=mkarray(new+2)
# # # new_line0=mkarray(new+2)
# # # for i in range(len(array)):
# # # array[i].insert(0,0)
# # # array[i].insert(len(array[i]),0)
# # # array.insert(0,new_line1)
# # # array.append(new_line0)
# # # rows=len(array)-1
# # # cols=len(array[0])-1
# # # row=rows-1
# # # col=cols
# # # iters=0
# # # while True:
# # # iters+=1
# # # print(col,cols,row)
# # # last_point+=1
# # # print(last_point)
# # # if row == rows and col == cols:
# # # array[row][col]=get_surrounders(array,[row,col])
# # # break
# # # if col == cols and row !=0:
# # # array[row][col]=get_surrounders(array,[row,col])
# # # array[row][col]=last_point
# # # row-=1
# # # continue
# # # if col == cols and row == 0:
# # # array[row][col]=last_point
# # # array[row][col]=get_surrounders(array,[row,col])
# # # col-=1
# # # continue
# # # if row==0 and col !=0:
# # # array[row][col]=last_point
# # # array[row][col]=get_surrounders(array,[row,col])
# # # col-=1
# # # continue
# # # if row==0 and col ==0:
# # # array[row][col]=last_point
# # # array[row][col]=get_surrounders(array,[row,col])
# # # row+=1
# # # continue
# # # if row != rows and col == 0:
# # # array[row][col]=last_point
# # # array[row][col]=get_surrounders(array,[row,col])
# # # row+=1
# # # continue
# # # if row == rows and col == 0:
# # # array[row][col]=last_point
# # # array[row][col]=get_surrounders(array,[row,col])
# # # col+=1
# # # continue
# # # if row == rows and col != cols:
# # # array[row][col]=get_surrounders(array,[row,col])
# # # array[row][col]=last_point
# # # col+=1
# # # continue
# #
# # # if x ==
# #
# # ##whole_line=list(range(last_point + 1, int(pow(math.sqrt(last_point) + 2,2)) + 1 ))
# # # denom=2
# # # while True:
# # ##y=len(array) -  denom
# # # x=
# # # last_point+=1
# # # array[y][x]=last_point
# # # print(iters)
# # # return array
# # # print(last_point)
# #
# #
# # # print(add_circle(drama))
# # # def check(array):
# # # for item in array:
# # # item.sort()
# # # for item1 in item:
# # # if item1 > 289326:
# # # print(item1)
# # # return True
# #
# # # ar=[[1]]
# #
# # # while True:
# # # ar=add_circle(ar)
# # # if check(ar):
# # # break
# # # for item in ar:
# # #print( item)
# # # print('---')
# #
# # # for i in ar:
# # # print(i)
# #
# # # ar[2][12]=65454851
# # # print(ar)
# #
# #
# # # day 4
# #
# #
# # # data=input1.split('\n')
# # # data = list(d.split(' ') for d in input1.split('\n'))
# # # app = []
# # # for item in data:
# # #     l1 = len(item)
# # #     item1 = set(item)
# # #     if len(item1) == l1:
# # #         app.append(item)
# # #
# # # ar1=[]
# # # appr=0
# # # for item in app:
# # #     new_line=[]
# # #     for word in item:
# # #         word1=list(word)
# # #         word1.sort()
# # #         word=''.join(word1)
# # #         if not word in new_line:
# # #             new_line.append(''.join(word))
# # #     if len(new_line) == len(item):
# # #         appr+=1
# # #
# # # print(appr)
# #
# #
# # # day 5
# # # day5 = list(map(lambda x: int(x), day5_raw.split('\n')))
# # #
# # #
# # # def jumps(data):
# # #     position = 0
# # #     jump = 0
# # #     while True:
# # #         if position < 0:
# # #             return jump
# #
# # # day 6
# # # from zlib import crc32
# # #
# # # data = day6_raw
# # #
# # #
# # # def infi_loop(data, results=[]):
# # #     def maximus():
# # #         current_max = 0
# # #         current_position =0
# # #         for i in range(len(data)):
# # #             if data[i] > current_max:
# # #                 current_max = data[i]
# # #                 current_position = i
# # #         return current_position
# # #
# # #
# # #     def iterator(position,summ):
# # #         if summ == 0:
# # #             return
# # #         if position == len(data):
# # #             position = 0
# # #         summ -= 1
# # #         data[position] += 1
# # #         position += 1
# # #         return iterator(position, summ)
# # #     a=0
# # #     checksums=[]
# # #     while True:
# # #         current_position=maximus()
# # #         a += 1
# # #         summ=data[current_position]
# # #         data[current_position]=0
# # #         iterator(current_position+1,summ)
# # #
# # #         current_checksumm =crc32(('/'.join(list(map(lambda x: str(x),data)))).encode())
# # #         if not current_checksumm in checksums:
# # #             checksums.append(current_checksumm)
# # #         else:
# # #             return a
# # #
# # #
# # # def infi_loop1(data, results=[]):
# # #     start=crc32(('/'.join(list(map(lambda x: str(x),data)))).encode())
# # #     def maximus():
# # #         current_max = 0
# # #         current_position =0
# # #         for i in range(len(data)):
# # #             if data[i] > current_max:
# # #                 current_max = data[i]
# # #                 current_position = i
# # #         return current_position
# # #
# # #     current_checksumm=0
# # #     def iterator(position,summ):
# # #         if summ == 0:
# # #             return
# # #         if position == len(data):
# # #             position = 0
# # #         summ -= 1
# # #         data[position] += 1
# # #         position += 1
# # #         return iterator(position, summ)
# # #     a=0
# # #     checksums=[]
# # #     while current_checksumm != start:
# # #         current_position=maximus()
# # #         a += 1
# # #         summ=data[current_position]
# # #         data[current_position]=0
# # #         iterator(current_position+1,summ)
# # #
# # #         current_checksumm =crc32(('/'.join(list(map(lambda x: str(x),data)))).encode())
# # #         # if not current_checksumm in checksums:
# # #         #     checksums.append(current_checksumm)
# # #         # else:
# # #     return a
# # #
# # # print(infi_loop(data))
# # # print(infi_loop1(data))
# #
# #
# # # day7
# #
# # def tower(line):
# #     array1 = line.split('\n')
# #     array2 = {}
# #     for item in array1:
# #         d = item.split('->')
# #         d1 = d[0].split()
# #         try:
# #             children = list(map(lambda x: x.strip(', '), (d[1]).split(',')))
# #         except:
# #             children = []
# #         name = d1[0]
# #         weight = int(d1[1].strip(')( '))
# #         array2[name] = [children, weight]
# #     bases = [f for f, val in array2.items() if val[0] != []]
# #     base_leafs = []
# #     for item in bases:
# #         for i in array2[item][0]:
# #             base_leafs.append(i)
# #     rf = []
# #     for item in sorted(bases):
# #         if item not in base_leafs:
# #             rf.append(item)
# #     return [rf[0], array2]
# #
# #
# # def balancer(basement, arr):
# #     position = 0
# #     ar1 = []
# #     ar2 = []
# #
# #     def walker(basement):
# #         current_programs = arr[basement][0]
# #         current_weight = arr[basement][1]
# #         if len(current_programs) == 0:
# #             return {'upper': 0, 'self': current_weight}
# #         weights = []
# #         for prog in current_programs:
# #             weights.append(walker(prog))
# #         uppers = []
# #         self_1 = []
# #         results1=[]
# #         for branch in weights:
# #             uppers.append(branch['upper'])
# #             self_1.append(branch['self'])
# #             results1.append(branch['upper']+branch['self'])
# #             # datas.append([self_1, self_1 + upper])
# #         if min(results1) != max(results1):
# #             print(uppers)
# #             print(self_1)
# #             print(results1)
# #         # try:
# #         #     sum(weights)
# #         # except:
# #         #     print(weights)
# #         return {'upper': sum(results1), 'self': current_weight}
# #
# #     walker(basement)
# #
# #
# # day7 = tower(day7_raw)
# #
# # # print(day7[1])
# #
# # print(balancer(day7[0], day7[1]))
#
#
# # day 8
#
#
# data8_raw = list(map(lambda x: x.split(), day8_raw.split("\n")))
#
#
# def day8_func(data8_raw):
#
#
#     data8 = {}
#     max1=0
#     data8_tmp = {}
#     def valuer():
#         if operation == 'inc':
#             data8_tmp[name]+=int(value)
#         else:
#             data8_tmp[name]-=int(value)
#     def maxer(max1):
#         if data8_tmp[name] > max1:
#             max1=data8_tmp[name]
#         return max1
#
#     position = 0
#     for item in data8_raw:
#         # data8_tmp[item[0]] = 0
#         data8[position] = {
#             'name': item[0],
#             'operation': item[1],
#             'value': item[2],
#             'condition': item[3],
#             'con_source1': item[4],
#             'con_type': item[5],
#             'con_val': item[6]
#         }
#         position += 1
#         name = item[0]
#         operation = item[1]
#         value = item[2]
#         condition = item[3]
#         con_source1 = item[4]
#         con_type = item[5]
#         con_val = item[6]
#         if name not in data8_tmp:
#             data8_tmp[name] = 0
#         if con_source1 not in data8_tmp:
#             data8_tmp[con_source1] = 0
#         if con_type == '<':
#             if data8_tmp[con_source1] < int(con_val):
#                 valuer()
#                 continue
#
#         elif con_type == '<=':
#             if data8_tmp[con_source1] <= int(con_val):
#                 valuer()
#                 max1=maxer(max1)
#                 continue
#         elif con_type == '==':
#             if data8_tmp[con_source1] == int(con_val):
#                 valuer()
#                 max1=maxer(max1)
#                 continue
#         elif con_type == '>=':
#             if data8_tmp[con_source1] >= int(con_val):
#                 valuer()
#                 max1=maxer(max1)
#                 continue
#         elif con_type == '>':
#             if data8_tmp[con_source1] > int(con_val):
#                 valuer()
#                 max1=maxer(max1)
#                 continue
#         elif con_type == '!=':
#             if data8_tmp[con_source1] != int(con_val):
#                 valuer()
#                 max1=maxer(max1)
#                 continue
#
#     return {'part1':max(list(f for p,f in data8_tmp.items())),'part2':max1}
# print(day8_func(data8_raw))
# # >
# # >=
# # !=
#
#
#
#
#
#
#
# #
# # print(data8_tmp)
# #
# # for position, value in data8.items():
# #     name = (value['name']),
# #     op = value['operation'][0],
# #     val = value['value'][0],
# #     cond = value['condition'][0],
# #     src = value['con_source1'][0],
# #     typ = value['con_type'][0],
# #     con_val = value['con_val'][0]
# #     # srv_val=data8_tmp[src]
# #     w_object = data8_tmp[name]
# #     print(w_object)
# #
# #
# # print(data8_tmp)


# DAY 9

# day9_raw = open('day9_input', 'r')
# day9 = list(day9_raw.read())
# day9_raw.close()
#
# # day9 = '{{{}}}'
#
#
# def bracketer(data):
#     o_brackets = 0
#     sum0 = 0
#     position = 0
#     garbage_count=0
#     counter = 0
#     garbage = 0
#     line_len = len(data)
#     i = 0
#     while i < line_len:
#         # print(o_brackets)
#         cur = data[i]
#         i += 1
#         if cur == '!':
#             i += 1
#             continue
#         if garbage != 0 and cur == ">":
#             garbage = 0
#             continue
#         if garbage == 1:
#             garbage_count +=1
#             continue
#         if cur == "<":
#             garbage = 1
#             continue
#         if cur == "{":
#             o_brackets += 1
#             sum0+=o_brackets
#             counter += 1
#             continue
#         if cur == "}":
#             o_brackets -= 1
#             continue
#         continue
#     return [sum0,garbage_count]
#
#
# print(bracketer(day9))

# Day 10
#
day10_ascii = [ord(f) for f in list(
    ','.join(map(lambda x: str(x), day10)))] + [17, 31, 73, 47, 23]


def knot_hash(input_line, rounds=1):
    def get_positions(start, rng):
        end = start + rng
        if end > len(working_list) - 1:
            start_part = list(range(start, len(working_list)))
            end_part = list(range(end - len(working_list)))
            return start_part + end_part
        return list(range(start, end))
    for _ in range(rounds):
        position = 0
        offset = 0
        working_list = list(range(256))
        for item in input_line:
            positions = get_positions(position, item)
            tmp_line = []
            for pos in positions:
                tmp_line.append(working_list[pos])
            tmp_line.reverse()
            for new in tmp_line:
                working_list[positions[0]] = new
                del(positions[0])
            position += (item + offset)
            while position > len(working_list) - 1:
                # print(position)
                position = position - len(working_list)
            offset += 1
    return {'list': working_list, 'part1': working_list[0] * working_list[1], 'pos': position, 'offset': offset}


day10_part1 = knot_hash(day10)
day10_part2 = knot_hash(day10_ascii, 64)
# print(day10_part2)

# n1 = []
# counter = 0
# new1_0 = []
# for item in day10_part2['list']:
#     # print(item)
#     if counter != 0 and counter % 16 == 0:
#         n1.append(new1_0)
#         # print(len(new1_0))
#         new1_0 = []
#     new1_0.append(item)
#     counter += 1

dense = []

for y in range(16):
    xor_list = day10_part2['list'][y*16:(y+1)*16]
    xor = xor_list[0]
    for i in range(1, len(xor_list)):
        xor = xor ^ xor_list[i]
    dense.append(xor)
print(dense)
s = ""
for x in dense:
    s += "{:02x}".format(x)

print(s)

# fline = ''
# for item in n1:
#     item1 = reduce((lambda x, y: x ^ y), item)
#     h_tmp = hex(item1).split('x')[-1]
#     if len(h_tmp) != 2:
#         h_tmp = '0' + h_tmp
#
#     fline += h_tmp
# print(fline)
#
# # for item in n1
#
# print(fline)
# #
# #
# # 00001100
# # 00000001
# # 00001101
# #
# # # part2 = knot_hash_2(
# #     day10_ascii, day10_part2['list'], day10_part2['pos'], day10_part2['offset'])
# # print(part2)
# # print(day10_part2['part1'])
# #
# # if day10_part2['list'] == part2[0]:
# #     print('Fuck!!!!')
# #
# # # day10_ascii=[ ord(f) for f in list(','.join(map(lambda x: str(x),day10)))] + [17, 31, 73, 47, 23]
# #
# # # print(day10_ascii)
