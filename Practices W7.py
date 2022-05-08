# -*- coding: utf-8 -*-
"""
Created on Mon May  2 10:59:03 2022

@author: Diana Armanikian
"""
#1. Yes, a Python list can hold a mixture of integers and strings.

#2. Python programming language supports negative indexing

#3.
A = [45, -3, 16, 8]

#4
lst = [10, -4, 11, 29]
#4.a
lst[0]
#4.b
lst[3]
#4.c lst[0] is 10
#4.d lst[3] is 29
#4.e lst[1] is -4
#4.f lst[-1] is 29
#4.g lst[-4] is 10
#4.h list indices must be integers or slices, not float

#5
lst = [3, 0, 1, 5, 2]
x = 2
#5.a lst[0] equals 3
#5.b lst[3] equals 5
#5.c lst[x] equals 1
#5.d lst[-x] equals 5
#5.e lst[x+1] equals 5
#5.f lst[x]+1 equals 2
#5.g lst[lst[x]] equals 0
#5.h lst[lst[lst[x]]] equals 3

#6 Python list method len() returns the number of elements in a list

#7 square backets which is: []

#8 
lst = [20, 1, -34, 40, -8, 60, 1, 3] 
#8.a lst equals [20, 1, -34, 40, -8, 60, 1, 3]
#8.b lst[0:3] equals [20, 1, -34]
#8.c lst[4:8] equals [-8, 60, 1, 3]
#8.d lst[4:33] equals [-8, 60, 1, 3]
#8.e lst[-5:-3] equals [40, -8, 60]
#8.f lst[-22:3] equals [20, 1, -34]
#8.g lst[4:] equals [-8, 60, 1, 3]
#8.h lst[:] equals [20, 1, -34, 40, -8, 60, 1, 3]
#8.i lst[:4] equals [20, 1, -34, 40]
#8.j lst[1:5] equals [1, -34, 40, -8, 60]
#8.k -34 in lst is true
#8.l -34 not in lst is false
#8.m len(lst) is 8
"""
#9 
  m  n
1.5  9
2.-5 -10
3.1  7
4.3  7
5.-
6.0  4
7.0  4
8.3  4  
9.0  1
10.1  3
11.0  4

"""

#10
a = [8] * 4 
#It equals [8,8,8,8]
b = 6 * [2,7]
#It equals [2, 7, 2, 7, 2, 7, 2, 7, 2, 7, 2, 7]
c = [1,2,3] + ['a','b','c','d']
#It equals [1, 2, 3, 'a', 'b', 'c', 'd']
d = 3 * [1,2] + [4,2]
#It equals [1, 2, 1, 2, 1, 2, 4, 2]
e = 3 * ([1,2] + [4,2])
#It equals [1, 2, 4, 2, 1, 2, 4, 2, 1, 2, 4, 2]

#11
a = [x+1 for x in [2,4,6,8]]
#[3, 5, 7, 9]
b = [10*x for x in range (5,10)]
#[50, 60, 70, 80, 90]
c = [x for x in range (10,21) if x%3 == 0]
#[12, 15, 18]
d = [(x,y) for x in range (3) for y in range (4)]
#[(0, 0), (0, 1), (0, 2), (0, 3), (1, 0), (1, 1), (1, 2), (1, 3), (2, 0), (2, 1), (2, 2), (2, 3)]
e = [(x,y) for x in range (3) for y in range (4) if (x+y)%2==0]
#[(0, 0), (0, 2), (1, 1), (1, 3), (2, 0), (2, 2)]

#12
a = [x**2 for x in range (1,6)]
b = [x+0.25 for x in [0,0.25,0.5,0.75,1,1.25]]
c = [(x,y) for x in ['a','b'] for y in range (3)]

#13 x in lst or x not in lst

#14 The reversed() function returns the reversed iterator of the given sequence 
#meaning python would be printed as 'n' 'o' 'h' 't' 'y' 'p'

#15
#    a=[3,-3,5,2,-1]
def sum_positive(a):
    s = 0 
    for x in a:
        if x > 0:
            s = s + x
    print (s)
 
#16
#    lst=[3,5,4,-1,0]
def count_evens(lst):
    c = 0
    for x in lst:
        if x % 2 == 0:
            c = c + 1
    print (c)
    
#17
def print_big_enough(List,secnum):
    for x in List:
        if x >= secnum:
            print (x)
            
#18
def next_number(lst,n):
    lst = [0,2,4,5]
    for i in lst:
        if i <= 0 or (len(set(lst))!=len(lst)):
            print("ERROR! Enter unique list with numbers higher than or equal to 1!")
            break
        for j in range(n-1): 
            if lst[j] == i:
                break

#19
mylist = ['a', 'b', 2, 5]
def reverse(mylist):
    mylist2 = []
    for item in mylist:
        mylist2.insert(0, item)
    return mylist2
print(reverse(mylist))
      
#20
def matrix(a,column):
    result = []
    for i in range(a):
        partial_result = []
        for i in range(column):
            partial_result.append(1)
        result.append(partial_result)
    return result
m = matrix(6, 9)
for i in m:
    print(i)
m[2][4] = 0
print("---------------------------")
for i in m:
    print(i)
    
#21
#1
def first_way():
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(a)


#2
def second_way():
    a = []

    for i in range(1, 11):
        a += [i]
    print(a)


#3
def third_way():
    a = []
    i = 1
    while i < 11:
        a.append(i)
        i += 1
    print(a)


def fourth_way():
    b = [-10, -9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    a = (b[3:13])
    print(a)


def fifth_way(n, a):
    if 11 > n > 0:
        a += [n]
        fifth_way(n + 1, a)
    return a

#22
game = [['O', 'X', 'O'],
        ['x', 'O', 'O'],
        ['x', 'O', 'O']]



def check_winner(game):
    
    if game[0][0] == game[0][1] and game[0][0] == game[0][2] and game[0][1] == game[0][2] and game[0][0] == 'x':
        result = 'x'
        return result
 
    if game[1][0] == game[1][1] and game[1][0] == game[1][2] and game[1][1] == game[1][2] and game[1][0] == 'x':
        result = 'x'
        return result
    
    if game[2][0] == game[2][1] and game[2][0] == game[2][2] and game[2][1] == game[0][2] and game[2][0] == 'x':
        result = 'x'
        return result
    
    if game[0][0] == game[1][0] and game[1][0] == game[2][0] and game[0][0] == game[2][0] and game[0][0] == 'x':
        result = 'x'
        return result

    if game[0][1] == game[1][1] and game[1][1] == game[2][1] and game[0][1] == game[2][1] and game[0][1] == 'x':
        result = 'x'
        return result

    if game[0][2] == game[1][2] and game[1][2] == game[2][2] and game[0][2] == game[2][2] and game[0][2] == 'x':
        result = 'x'
        return result

    if game[0][0] == game[1][1] and game[1][1] == game[2][2] and game[0][0] == game[2][2] and game[0][0] == 'x':
        result = 'x'
        return result
    
    if game[0][2] == game[1][1] and game[1][1] == game[2][0] and game[0][2] == game[2][0] and game[0][2] == 'x':
        result = 'x'
        return result
    else:
        result = ' '
        return result


print(check_winner(game))













