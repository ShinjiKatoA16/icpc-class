#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

n = int(sys.stdin.readline())

def factorial(val):
    ret = 1
    for i in range(1, val+1):
        ret *= i
    return ret


for i in range(n):
    val = int(sys.stdin.readline())
    print(factorial(val))
