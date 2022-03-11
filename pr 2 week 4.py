max_value = int(input('Display primes up to what value? '))
value = 2
for value in range (2, max_value +1):
    is_prime = True 
    for trial_factor in range (2, value):
        if value % trial_factor == 0:
            break
    else:
        print(value, end= ' ')
print ()