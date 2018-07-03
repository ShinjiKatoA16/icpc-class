#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

def solve(n1, n2, max_capa):
    load = n1+1
    while (load % n1 == 0) or (load % n2 == 0):
        load += 1
    print(max_capa // load)

num_tc = int(sys.stdin.readline())
for i in range(num_tc):
    n1, n2, max_capa = map(int, sys.stdin.readline().split())
    solve(n1, n2, max_capa)
