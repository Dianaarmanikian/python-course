val = int(input())
if val < 10:
        if val != 5:
                print('wow ', end='')
        else:
                val += 1
else: 
        if val == 17:
                val += 10
        else:
                print("whoa ", end='')
        print(val)
#for 3 it prints "wow"
#for 21 it prints "whoa 21"
#for 5 it doesn't print anything
#for 17 it prints "27"
#for -5 it prints "wow"