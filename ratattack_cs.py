#!/usr/bin/python3
# -*- coding: utf-8 -*-

MAP_SIZE = 1025

import sys


def solve(rat_loc, bomb_power):  # Full Search version
    # map[x][y] shows size of rat
    map = [[0 for y in range(MAP_SIZE)] for x in range(MAP_SIZE)]
    for rat in rat_loc:
        x, y, size = rat
        map[x][y] = size

    max_kill = 0
    for x in range(MAP_SIZE-bomb_power):
        for y in range(MAP_SIZE-bomb_power):
            kill_size = 0
            for _x in range(max(0,x-bomb_power), x+bomb_power+1):
                for _y in range(max(0,y-bomb_power), y+bomb_power+1):
                    kill_size += map[_x][_y]
            if kill_size > max_kill:
                pos_x = x
                pos_y = y
                # print('updated', pos_x, pos_y, max_kill, kill_size)
                max_kill = kill_size

    print(pos_x, pos_y, max_kill)



num_tc = int(sys.stdin.readline())
for i in range(num_tc):
    bomb_power = int(sys.stdin.readline())
    num_rat_loc = int(sys.stdin.readline())
    rat_loc = list()
    for n in range(num_rat_loc):
        x,y,size = map(int, sys.stdin.readline().split())
        rat_loc.append([x,y,size])
    solve(rat_loc, bomb_power)
