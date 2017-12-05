import sys
import t_data
from time import time


def dailyTemperatures1(temperatures):
    t = time()
    long_ar = []
    longitude = len(temperatures)

    def lam(array, point, position, count):
        if position >= longitude:
            return 0
        elif array[position] > array[point]:
            return count
        return lam(array, point, position + 1, count + 1)
    while True:
        steps = 0
        current = temperatures[0]
        del(temperatures[0])
        if max(temperatures) <= current:
            long_ar.append(0)
            continue
        for i in range(len(temperatures)):
            steps += 1
            if current > temperatures[i]:
                long_ar.append(steps)
    print(time.time() - t)
    return long_ar


data = [73, 74, 75, 71, 69, 72, 76, 73]

# for item in data:
#     print(item, type(item))


def dailyTemperatures2(tem):
    tmp = [[], []]
    # tmp1=[]
    mx = max(tem)
    result = list()
    for i in range(len(tem)):
        current = tem[i]
        append = 1
        if current == mx:
            result.append([i, 0])
            append = 0
        for r in tmp[0]:
            pos, val, step = r
            step += 1
            if current > val:
                result.append([pos, step])
                # tmp.remove(r)
                continue

            tmp[1].append([pos, val, step])
        # for ir in tmp:
            # if ir == 0:
            # tmp.remove(ir)
        if append == 1:
            tmp[1].append([i, current, 0])
        # tt=time()
        tmp[0], tmp[1] = tmp[1], []
        # tmp[1]=[]
        # print(time()-tt)
    for item in tmp[0]:
        result.append([item[0], 0])
    print(result)

    # for i in range(len(tem)):
    # no_append=0
    # if tem[i] == mx:
    # result.append([i,0])
    # no_append=1
    # for item in tmp:
    # position,value,steps=item
    # print(position,steps)
    # if tem[i] > value:
    # if position == 3:
    # print(steps)
    #result.append([position,steps + 1])
    # tmp.remove(item)
    # continue
    # tmp.remove([position,value,steps])
    #tmp.append([position,value,steps + 1])
    # if no_append == 0:
    # tmp.append([i,tem[i],0])
    l = []
    ##print(time() - t)
    # if not tmp == []:
    # for item in tmp:
    # position=item[0]
    # result.append([position,0])
    result.sort(key=lambda x: x[0])

    for item in result:
        l.append(item[1])
    return result


def daily(tem):
    print(len(tem))
    tmp = {}
    t = time()
    keys = []
    r_list = {}
    r_list1 = []
    t1=time()
    for i in range(len(tem)):
        dat = tem[i]
        if not dat in tmp:
            tmp[dat] = [i]
        else:
            tmp[dat].append(i)
    print('Parsing time:',time()-t1)
    for k in tmp:
        keys.append(k)
    print(keys)
    for k in keys:
        keys_t = list(d for d in keys if d > k)
        tem_positions=[]
        for item in keys_t:
            for k,v in tmp.items():
                tem_positions+=v

        # t12=time()
        tem_positions.sort()
        print(type(tem_positions[0]))
        for item in tmp[k]:
            # t12=time()/

            # for nested_root in keys_t:
            #     for nested in tmp[nested_root]:
            #         delta = nested - item
            #         if delta > 0 and delta < r_list[item]:
            #             r_list[item] = delta
            #             continue
            for i in tem_positions:
                if i > item:
                    r_list[item]=i
                    break
    for key, value in r_list.items():
        if value == 66666666666666666666666666666666666:
            value = 0
        r_list1.append(value)


    # print(r_list1)
    print('overall time:',time() - t)

    # print(keys_t/



    # print(dailyTemperatures2(data))
    # print(dailyTemperatures(data))
daily(t_data.data0)
