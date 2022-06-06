# -*- coding: utf-8 -*-
"""
Created on Sat May 28 23:34:06 2022
w8p12
@author: Diana Armanikian
"""
#11.
try:
    lst = [0, 0, 0, 0]
    with open('data.txt', 'r') as f:
        count = 0
        for line in f.readlines():
            lst[count] = int(line)
            count += 1
except FileNotFoundError:
    print("Couldn't place the file sadly.")
#12. a
try:
    print('Begin')
    x = int(input())
    print(x)
    print('End')
except ValueError:
    print("Enter integer")
#i. 22
#ii. ValueError: invalid literal for int() with base 10: 'ZZ'

#12. b
print('Begin')
try:
    x = int(input())
    print(x)
except ValueError:
    print('Wrong!')
print('End')
#i. 22
#ii. Wrong !

#12. c
print('Begin')
try:
    x = int(input())
    print(x)
except IndexError:
    print('Wrong!')
print('End')
#i. 22
#ii. ValueError: invalid literal for int() with base 10: 'ZZ'
#12. d
"""
i. User enters 22  ==> 22
ii. User enters ZZ ==> Wrong!
"""
# there is noting to change!

print('Begin')
try:
    x = int(input())
    print(x)
except Exception:
    print('Wrong!')
print('End')
"----------------------------------------------------------------------------------------------------------------------"
#12. e
"""
i. User enters 22  ==> 22
                       wow
ii. User enters ZZ ==> Wrong!
"""
# there is noting to change!

print('Begin')
try:
    x = int(input())
    print(x)
except ValueError:
    print('Wrong!')
else:
    print('Wow')
print('End')
"----------------------------------------------------------------------------------------------------------------------"
#12. f
"""
i. User enters 22  ==> 22
                       Done
ii. User enters ZZ ==> Wrong!
                       Done
"""
# there is noting to change!

print('Begin')
try:
    x = int(input())
    print(x)
except ValueError:
    print('Wrong!')
finally:
    print('Done')
print('End')
"----------------------------------------------------------------------------------------------------------------------"
#12. g
"""
i. User enters 22  ==> 22
                       Wow
                       Done 
ii. User enters ZZ ==> Wrong!
                       Done
"""
# there is noting to change!

print('Begin')
try:
    x = int(input())
    print(x)
except ValueError:
    print('Wrong!')
else:
    print('Wow')
finally:
    print('Done')
print('End')

"""
13. What is the problem with the following code?
answer : 'Exception', superclass of the exception class 'ValueError', has already been caught
"""


def f():
    pass


try:
    f()  # Function f can raise an exception
except Exception:
    print(1)
except ValueError:
    print(2)
""" its better :
except ValueError:
    print(2)
except Exception:
    print(1)
"""

"""
14. What is the problem with the following code?
answer : 'OSError', superclass of the exception class 'FileNotFoundError', has already been caught
"""


def f():
    pass


try:
    f()  # Function f can raise an exception
except OSError:
    print(1)
except FileNotFoundError:
    print(2)
""" its better :
except FileNotFoundError:
    print(2)
except OSError:
    print(1)
"""














