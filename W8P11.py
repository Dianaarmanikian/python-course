# -*- coding: utf-8 -*-
"""
Created on Tue May 24 14:51:53 2022
w8 
@author: Diana Armanikian
"""
#11.11 exercises
#1. Tuples are different from sets A tuple is an immutable ordered structure. 
#You cannot change its length to add more things to it. 
#A list is a mutable ordered structure.

#2. In Python, lists and tuples are declared in different ways. 
#A list is created using square brackets [] 
#whereas the tuple is created using parenthesis ()

#3. tuples are immutable

#4. they are unordered in tuples

#5. 
a = 1, 2, 3, 4, 5, 6, 7, 8
_, _, *s, _, _ = a
print(s)
#prints [3, 4, 5, 6]

#6.
a = 1, 2, 3, 4, 5, 6, 7, 8
s = a[3:7]
print(s)
#prints (4, 5, 6, 7)

#7.
tpl= 7, 10, -3, 18, 6, 10
x, _, _, _, _, y = tpl
print(x, y)
#prints 7 10

#8.
def product(val):
    r = 1
    for elements in val:
        r *= elements
    return r
test_tup = (2.5, 2, 10)
r = product(list(test_tup))
print("The product of tuple elements are: " + str(r))
#prints The product of tuple elements are : 50.0

#9.
def zerosum(val):
    r = 0
    for elements in val:
        r += elements
    if r == 0:
        return True
    else:
        return False
test_tup = (2,-2, 4)    
r = zerosum(list(test_tup))
print(r)
#returns false

#10. A dictionary is sometimes called an associative array because 
#it associates a key with an item

#11.
d = {}

#12.
d = {"Fred":1}
print(d["Fred"])
#prints 1

#13. KeyError: 'the name of the wrong key'

#14. KeyError ...

#15. dictionaries are mutable

#16. a ~> {3:0, 5:1, 10:1, 8:2, 15:4}
"""
b:
    1
    3
    5
    10
    8
    15

c:
    1
    3
    5
    10
    8
    15

d:
    1
    0
    1
    1
    2
    4
"""

#17. dictionaries are unordered

d = {3:0, 5:1, 10:1, 8:2, 15:4}
for x in d.values():
    print(x)

#18 & 19 are in a different file

#20. because {} creates an empty dictionary

#21.
A = set()

#22. sets are mutable in py.

#23.
A = {20, 19, 2, 10, 7}
B = {4, 10, 5, 6, 9, 7}
C = {10, 19}
"""
a: {2, 7, 10, 19, 20}
b: True
c: False
d: {10, 7}
e: {2, 4, 5, 6, 7, 9, 10, 19, 20}
f: True
g: True
h: False
i: True
j: False
k: 5
l: {2, 3, 4, 5, 6, 7, 8, 9, 10, 11}
m: {0, 5, 8, 17, 18}
n: {0, 5}  
"""























    