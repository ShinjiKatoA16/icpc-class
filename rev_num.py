#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

n = int(sys.stdin.readline())
for i in range(n):
    s1, s2 = sys.stdin.readline().split()
    s1r = s1[::-1]
    s2r = s2[::-1]
    print(str(int(str(int(s1r) + int(s2r))[::-1])))
