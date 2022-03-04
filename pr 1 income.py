income = int (input('Please enter your income: '))
if income < 1000:
    print('Your tax rate is 0% therefore your net income is:', income)
if income > 1000 and income <= 2500:
    print ('Your tax rate is 10% therefore your net income is:', income*0.90)
if income > 2500 and income <= 4000:
    print ('Your tax rate is 15% therefore your net income is:', income*0.85)
if income > 4000 and income <= 6000:
    print ('Your tax rate is 20% therefore your net income is:', income*0.80)
if income > 8000:
    print ('Your tax rate is 30% therefore your net income is:', income*0.70)
