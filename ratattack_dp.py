#!/usr/bin/python3
# -*- coding: utf-8 -*-

MAP_SIZE = 1025

import sys


def solve(rat_loc, bomb_power):  # Dynamic program version
    # map[x][y] shows bomb kills rat
    map = [[0 for y in range(MAP_SIZE)] for x in range(MAP_SIZE)]
    for rat in rat_loc:
        x, y, size = rat
        for _x in range(max(0,x-bomb_power), min(MAP_SIZE,x+bomb_power)):
            for _y in range(max(0,y-bomb_power), min(MAP_SIZE,y+bomb_power)):
                map[_x][_y] += size

    max_kill = [0, 0, 0]  # Row, Col, Size
    for x in range(MAP_SIZE-bomb_power):
        for y in range(MAP_SIZE-bomb_power):
            if map[x][y] > max_kill[2]:
                max_kill = [x, y, map[x][y]]

    print(max_kill[0], max_kill[1], max_kill[2])



num_tc = int(sys.stdin.readline())
for i in range(num_tc):
    bomb_power = int(sys.stdin.readline())
    num_rat_loc = int(sys.stdin.readline())
    rat_loc = list()
    for n in range(num_rat_loc):
        x,y,size = map(int, sys.stdin.readline().split())
        rat_loc.append([x,y,size])
    solve(rat_loc, bomb_power)
