print ('Please enter 3 angles one by one: ')
angle1 = int (input('Enter the first angle: '))
angle2 = int (input('Enter the second angle: '))
angle3 = int (input('Enter the last angle: '))
sum = angle1+angle2+angle3
if sum != 180 :
    print ('Your angles do not add up to 180, NOT A TRIANGLE')
    quit ()
if angle1==180 or angle2==180 or angle3==180 or angle1==0 or angle2==0 or angle3==0 :
    print ('Wrong angles, NOT A TRIANGLE')
    quit ()
if angle1==90 or angle2==90 or angle3==90 :
    print ('Right')
else : print ('NOT Right')