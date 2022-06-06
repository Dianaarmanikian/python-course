# -*- coding: utf-8 -*-
"""
Created on Mon Jun  6 07:13:07 2022
W8P13
@author: Diana Armanikian
"""
"""
1. Given the definition of the geometric Point class, complete the function named distance:
def distance(r1, r2):
# Details go here
that returns the distance between the two points passed as parameters.
"""
import math


def distance(r1, r2):
    d = math.sqrt((r2[0] - r1[0]) ** 2 + (r2[1] - r1[1]) ** 2)
    return d


# (x , y) for example :
print(distance((1, 2), (4, 2)))

"""
3. What is the purpose of the __init__ method in a class? answer :
The __init__ function is called every time an object is created from a class.
The __init__ method lets the class initialize the object's attributes and serves no other purpose.
"""

"""
5. Given the definition of the Rational number class, complete the following method named reduce:
class Rational:
    # Other details omitted here ...
    # Returns an object of the same value reduced
    # to lowest terms
    def reduce(self):
        # Details go here
"""
from functools import reduce
from math import gcd

num1 = input('insert first number : ')
num2 = input('insert second number : ')
print(num1, '/', num2)
ratio = num1 + '/' + num2


class Rational():
    def __init__(self, ratio):
        self.ratio = ratio

    def solve(self):
        numbers = [int(i) for i in self.ratio.split('/')]
        denominater = reduce(gcd, numbers)
        solved = [i / denominater for i in numbers]
        return '/'.join(str(i) for i in solved)


Numbers = Rational(ratio)
print(Numbers.solve())

"""
7. Given the definition of the geometric Point class, add a method named distance:
"""
import math


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def doubledistance(self, p):
        d = math.sqrt((a.x - p[0]) ** 2 + (a.y - p[1]) ** 2)
        return d


if __name__ == '__main__':
    a = Point(2, 3)
    print(a.doubledistance((3, 3)))
    
"""
9. Develop a Circle class that, like the Rectangle class above, provides methods to compute perimeter
and area. The Rectangle instance variables are not appropriate for circles; specifically, circles do
not have corners, and there is no need to specify a width and height. A center point and a radius more
naturally describe a circle. Build your Circle class appropriately.
"""


class Circle():
    def __init__(self, radius):
        self.radius = int(radius)

    def perimeter(self):
        p = self.radius * 2 * 3.141
        return p

    def area(self):
        a = self.radius ** 2 * 3.141
        return a


myCircle = Circle(int(input("insert circle radius : ")))
print('perimeter : ', myCircle.perimeter())
print('area : ', myCircle.area())

"""
11. Consider the following Python code:
(a) What does the program print? answer :
40
0
41
1
50
2
(b) If wid is a Widget object, what is the minimum value the expression wid.get() can return? 0
(c) If wid is a Widget object, what is the maximum value the expression wid.get() can return? ∞ (Infinity)
"""


class Widget:
    def __init__(self, v=40):
        if v >= 40:
            self.value = v
        else:
            self.value = 0

    def get(self):
        return self.value

    def bump(self):
        if self.value < 50:
            self.value += 1


def main():
    w1 = Widget()
    w2 = Widget(5)
    print(w1.get())
    print(w2.get())
    w1.bump()
    w2.bump()
    print(w1.get())
    print(w2.get())
    for i in range(20):
        w1.bump()
    w2.bump()
    print(w1.get())
    print(w2.get())


if __name__ == '__main__':
    main()