
"""
Created on Sat Apr 14 16:41:36 2022
Hanoi Tower 
@author: Diana Armanikian
"""
def TowerOfHanoi(n , from1, to, aux):
    if n==1:
        print ("Move disk 1 from ",from1,"to ",to)
        return
    TowerOfHanoi(n-1, from1, aux, to)
    print ("Move disk",n,"from ",from1,"to ",to)
    TowerOfHanoi(n-1, aux, to, from1)

n = int(input("Enter the number of the disks: "))
TowerOfHanoi(n,'A','C','B')
