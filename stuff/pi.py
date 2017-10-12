#!/usr/bin/env python3
from factorial import factorial
from new_pow import pow
import math
import sys
from fractions import Fraction
from rationals import make, summ, minus, multiply
sys.setrecursionlimit(100000)


def pi1(rounds):
    multiplier = 1 / (426880 * math.sqrt(10005))
    answer = 0
    k = 0
    while k <= rounds:
        answer += (factorial(6 * k) * (13591409 + (545140134 * k))) / \
            (factorial(3 * k) * pow(factorial(k), 3) * pow(-640320, 3 * k))
        k += 1
    return answer * multiplier


def pi2(rounds):
    def worker(k, accum):
        if k > rounds:
            return accum
        k8 = 8 * k
        data = Fraction(1, pow(16, k)) * (Fraction(4, k8 + 1) -
                                          Fraction(2, k8 + 4) - Fraction(1, k8 + 5) - Fraction(1 / k8 + 6))
        return worker(k + 1, accum + data)
    return worker(0, Fraction(1, 1))


def pi3(rounds):
    def worker(k, accum):
        if k > rounds:
            return car(accum) / cdr(accum)
        k8 = 8 * k
        try:
            m4 = minus(make(1, k8 + 5), make(1, k8 + 6))
        except:
            print('m3')
        m3 = minus(make(4, k8 + 1), make(2, k8 + 4))
        try:
            m2 = minus(m3, m4)
        except:
            print('m2')
        data = multiply(m1, m2)
        return worker(k + 1, accum + data)
    return worker(0, make(1, 1))


def pi4(rounds):
    def worker(k, accum):
        if k > rounds:
            return accum
        k8 = 8 * k
        data = (1 / pow(16, k)) * ((4 / (k8 + 1)) -
                                   (2 / (k8 + 4)) - (1 / (k8 + 5)) - (1 / (k8 + 6)))
        return worker(k + 1, accum + data)
    return worker(0, 0)


print(format(pi4(456), '.10000040g'))
