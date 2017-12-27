#!/bin/python

import sys

def gameOfThrones(s):
    # Complete this function
    dictionary = {}
    flag = 0
    for i in s:
        if i in dictionary:
            dictionary[i] += 1
        else:
            dictionary[i] = 1

    #print("The value in the ditionary is ",dictionary)
    for i in dictionary:
        #print(i,dictionary[i])
        if (dictionary[i]%2 != 0):
            flag += 1

    if flag >1:
        return "NO"
    else:
        return "YES"

s = raw_input().strip()
result = gameOfThrones(s)
print(result)