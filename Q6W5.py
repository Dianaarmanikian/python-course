# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 06:01:52 2022
@author: Diana Armanikian
sixth question
"""
n = float(input("Enter number: "))
if n < 0:
    exit()
maximum, minimum = n, n
avg, s, count = 0, n, 1
while True:
    n = float(input("Enter number: "))
    if n < 0:
        break
    s += n
    count += 1
    if n > maximum:
        maximum = n
    if n < minimum:
        minimum = n
avg = s / count
print("Sum = {0}, Average = {1}, Max = {2}, Min = {3}".format(s, avg, maximum, minimum))
