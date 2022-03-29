# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 23:28:33 2022
@author: Diana Armanikian
third question
"""
for i in range(1, 10001):
    t = i
    s = 0
    c = 0
    while t != 0:
        c += 1
        t //= 10
    t = i
    while t != 0:
        r = t % 10
        s += r ** c
        t //= 10
    if i == s:
        print(i)

