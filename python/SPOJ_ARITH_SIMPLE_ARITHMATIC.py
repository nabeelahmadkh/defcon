# Python Program for SPOJ Problem Number 6 (ArithMatic).
# Code started on 17/07/2017
# Last Edit on 17/07/2017
# Code by Nabeel Ahmad Khan


import math
import re

x=raw_input ("Enter the string")   #raw input to avoid the mathmatical operation 
print

regex = "[+-/*]"
first, second = re.split(regex, x)
len1=len(first)             # first calculate the length of the string 
len2=len(second)
first = int(first)          # then convert the string into integer for Math operations
second = int(second)

match = re.findall(regex,x) # to find the operator used for mathmatical operation

if len1>len2:
    max=len1
else:
    max=len2

j=len1
while(j<max+1):
    print "",               # printing the spaces for the first input
    j+=1    
print first                 # priting the first input 

j=len2
while(j<max+1):
    print "",               # printing the spaces for the second input
    j+=1 
print second                # priting the second input 

third = match[0]

if len1>len2:
    for i in range(0,len1):
        third = third+"-"
else:
    for i in range(0,len2):
        third = third+"-"

print third                 # printing the operator"[+-*/]" and dashes "-" accordingly

if match[0] == '+':
    answer = first + second
    answerStr=str(answer)
    len3=len(answerStr)
    j=len3
    while(j<max+1):
        print "",
        j+=1
    print answer            # priting the last output

elif match[0] == '-':
    answer = first - second
    answerStr=str(answer)
    len3=len(answerStr)
    j=len3
    while(j<max+1):
        print "",
        j+=1
    print answer            # priting the last output

elif match[0] == '*':
    answer = first * second
    answerStr=str(answer)
    len3=len(answerStr)
    j=len3
    while(j<max+1):
        print "",
        j+=1
    print answer            # priting the last output

else:
    answer = first / second
    answerStr=str(answer)
    len3=len(answerStr)
    j=len3
    while(j<max+1):
        print "",
        j+=1
    print answer            # priting the last output



    



