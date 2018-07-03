#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

def solve(month, week, day_of_month):
    dom = day_of_month[month]
    dom -= 28
    week_end = 8

    if week == 'SUN' and dom >= 1:
        week_end += 1
    if week == 'SAT':
        if dom == 1:
            week_end += 1
        elif dom > 1:
            week_end += 2
    if week == 'FRI':
        if dom == 2:
            week_end += 1
        elif dom > 2:
            week_end += 2
    if week == 'THU':
        if dom > 2:
            week_end += 1

    print(week_end)

day_of_month = {'JAN':31, 'FEB':28, 'MAR':31, 'APR': 30, 'MAY':31, 'JUN':30,
                'JUL':31, 'AUG':31, 'SEP':30, 'OCT': 31, 'NOV':30, 'DEC':31}

num_tc = int(sys.stdin.readline())
for i in range(num_tc):
    month, week = sys.stdin.readline().split()
    solve(month, week, day_of_month)
