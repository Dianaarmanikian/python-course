# -*- coding: utf-8 -*-
"""
Created on Mo'0n Mar 28 23:12:10 2022
@author: Diana Armanikian
first question
"""
x = float(input())
a, b, f, s, sin = x, 1, 2, 1, x
for i in range(30):
    a *= x * x
    b *= f * (f + 1)
    f += 2
    s *= -1
    sin += s * a / b
print("Sin({0}) = {1}".format(x, sin))

