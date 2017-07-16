# Python Program for printing the prime numbers upto n.
# Code started on 14/07/2017
# Last Edit on 14/07/2017
# Code by Nabeel Ahmad Khan 

import math

def checkPrime(n):
    m=math.sqrt(n)
    m=int(m) + 1
    check=0
    
    for j in range(2, m):
        if n%j == 0:
            check=1
            break

    if check == 0:
        return n

def sieveOfErathosthenos(x):
    array = [True] * (x+1)
    print array
    for j in range(2, int(math.sqrt(x))+1):
        if (array[j] == True):
            for k in range(j*2, x+1, j):
                array[k]=False
    for l in range(2,x):
        if array[l] == True:
            print "the prime numbers are ",l


    
x = input("Enter the number upto which prime numbers are to be displayed")
print x

a=10
b=5
print a,b
a,b = b,a #for swapping by XOR method
print "after swapping the value of a & b are ",a ,b

#for i in range(2,x+1):
#    disp=checkPrime(i)
#    if disp:
#        print disp, "is a prime"

sieveOfErathosthenos(x)

