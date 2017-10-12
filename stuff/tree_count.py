#!/usr/bin/python3
# this

import random
import sqlite3


result = []
tmp_id = 0


def tup_tree(levels, deep=5, pid=0):
    global result
    global tmp_id
    for level in range(1, levels + 1):
        parent_id = tmp_id
        result.append({'id': tmp_id, 'name': 'name', 'pid': pid})
        tmp_id += 1
        if (deep > 1):
            tup_tree(levels, deep - 1, parent_id)
    return result


def count_tree(levels, deep, type=1):
    if (type == 1):
        acc = 0
        for f in range(0, deep + 1):
            acc = acc * levels + levels * f
        return acc
    elif (type == 2):
        power = deep
        acc = 0
        for f in range(1, deep + 1):
            acc = acc + f * pow(levels, power)
            power -= 1
        return acc
    else:
        acc = levels
        for f in range(2, deep + 1):
            acc = (acc + f) * levels
        return acc


print(count_tree(30, 666, 2))


def tup_stan():
    data = ""
    a = 1
    b = '"dsfsdfsdoiuy876frcvtbgy87h6857rxcvtbyhu8hj90"'
    with sqlite3.connect('rtbase') as base:
        base.execute('drop table if exists t1')
        base.execute(
            'create table if not exists t1 (id INT,name TEXT, pid INT)')
        cur = base.cursor()
        while a <= 120000000:
            c = random.randrange(1, 66666)
            cur.execute("""insert into t1 values (?,?,?)""", (a, b, c))
            a += 1
