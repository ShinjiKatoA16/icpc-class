#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

def simulate(eat, num_candie):
    print('Try', eat, 'per day', end = ' ', file=sys.stderr)
    half_or_more = (num_candie+1) // 2
    vasis_eat = 0

    while(num_candie > 0):
        v_eat = min(eat, num_candie)
        vasis_eat += v_eat
        num_candie -= v_eat
        p_eat = (num_candie // 10)
        num_candie -= p_eat
        print(v_eat, ':', p_eat, sep='', end=' ', file=sys.stderr)

    if vasis_eat >= half_or_more:
        print('OK:', vasis_eat, file=sys.stderr)
        return True
    else:
        print('NG:', vasis_eat, file=sys.stderr)
        return False


def solve(num_candie):
    max_ng = 0
    min_ok = num_candie

    while min_ok > max_ng + 1:
        eat = (min_ok + max_ng) // 2
        if simulate(eat, num_candie):
            min_ok = eat
        else:
            max_ng = eat

    print(min_ok)


num_tc = int(sys.stdin.readline())
for i in range(num_tc):
    solve(int(sys.stdin.readline()))
