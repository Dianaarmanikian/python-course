#if i=3 j=5 k=7 result: i = 5  j = 5  k = 7
#if i=3 j=7 k=5 result: i = 3  j = 5  k = 5
#if i=5 j=3 k=7 result: i = 7  j = 3  k = 7
#if i=5 j=7 k=3 result: i = 5  j = 3  k = 3
#if i=7 j=3 k=5 result: i = 5  j = 3  k = 5
#if i=7 j=5 k=3 result: i = 7  j = 7  k = 3
i=7
j=5
k=3
if i<j:
    if j<k:
        i = j
    else:
        j = k
else:
    if j>k:
        j = i
    else:
        i = k
print ("i =", i," j =", j," k =", k)