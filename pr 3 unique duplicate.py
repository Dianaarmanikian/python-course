print ('Please enter 5 integers one by one: ')
a = int (input('Enter the first int: '))
b = int (input('Enter the second int: '))
c = int (input('Enter the third int: '))
d = int (input('Enter the fourth int: '))
e = int (input('Enter the last int: '))
if a == b or a == c or a == d or a == e or b == c or b == d or b == e or c == d or c == e or d == e:
    print ('DUPLICATES')
else : print ('All UNIQUE')