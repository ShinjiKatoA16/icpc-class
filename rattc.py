#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import random

MAX_POS = 1025
MAX_BOMB_POWER = 10
MAX_RAT_LOC = 200

print(1)
print(random.randrange(1,MAX_BOMB_POWER+1))
n_rat = random.randrange(1,MAX_RAT_LOC+1)
print(n_rat)

rats = dict()
for i in range(n_rat):
    while True:
        x = random.randrange(MAX_POS)
        y = random.randrange(MAX_POS)
        if (x,y) not in rats:
            rats[(x,y)] = True
            print(x,y,random.randrange(1,256))
            break

        
