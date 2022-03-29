# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 23:32:05 2022
@author: Diana Armanikian
fifth question
"""
text = input("Enter text: ")
num = int(input("Enter number: "))
a = list(text)
for i in range(len(a)):
    if 'a' <= a[i] <= 'z':
        c = ord(a[i])
        c += num
        if c > 122:
            c -= 26
        print(chr(c), end="")
    elif 'A' <= a[i] <= 'Z':
        c = ord(a[i])
        c += num
        if c > 90:
            c -= 26
        print(chr(c), end="")


