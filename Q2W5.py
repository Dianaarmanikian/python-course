# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 23:27:38 2022
@author: Diana Armanikian
second question
"""
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
while b != 0:
    t = a
    a = b
    b = t % b
print("GCD:", a)

