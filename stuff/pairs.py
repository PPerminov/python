#!/usr/bin/env python3
def pair(car, cdr):
    def selector(getter):
        if getter == 'car':
            return car
        return cdr
    return selector


def car(pair):
    return pair('car')


def cdr(pair):
    return pair('cdr')
