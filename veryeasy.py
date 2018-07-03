#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

for s in sys.stdin:
    n,a = map(int, s.split())

    result = 0
    for i in range(1,n+1):
        result +=  i * a ** i

    print(result)
