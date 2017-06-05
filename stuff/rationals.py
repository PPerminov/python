#!/usr/bin/env python3

from pairs import pair, car, cdr

def make(numerator,denominator):
    if denominator < 0:
        numerator = 0 - numerator

def summ(r1,r2):
    numerator = (car(r1) * cdr(r2)) + (car(r2) * cdr(r1))
    denominator = cdr(r1) * cdr (r2)
    return pair(numerator,denominator)

def minus(r1,r2):
    numerator = (car(r1) * cdr(r2)) - (car(r2) * cdr(r1))
    denominator = cdr(r1) * cdr (r2)
    return pair(numerator,denominator)

def multiply(r1,r2):
    numerator = (car(r1) * car(r2))
    denominator = cdr(r1) * cdr (r2)
    return pair(numerator,denominator)
