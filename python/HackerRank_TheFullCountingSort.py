#!/bin/python

import sys

# q = int(raw_input())
# s1 = []
# for a0 in xrange(q):
#     temp = raw_input()
#     s1.append(temp)

intArray = []
strArray = []
dictionary = {}
finalOutput = ""

# Sample cases
q =20
s1 = ["0 ab", "6 cd", "0 ef", "6 gh", "4 ij", "0 ab", "6 cd", "0 ef", "6 gh", "0 ij", "4 that", "3 be", "0 to", "1 be", "5 question", "1 or", "2 not", "4 is", "2 to", "4 the"]

for i in s1:
    temp = i.split(" ")
    intArray.append(int(temp[0]))
    strArray.append(str(temp[1]))

for i in range(len(strArray)/2):
    dictionary[strArray[i]] = True



# print("IntArray is ",intArray)
# print("StrArray is ",strArray)

temp2 = sorted(range(len(intArray)), key=lambda k: intArray[k])

#num = numpy.array(intArray)
#strg = numpy.array(strArray)
#temp = num.argsort(kind='mergesort') # create a list of index where the object should be placed, merge sort makes it stable sort
#sortedPeople = strg[temp]

sortedPeople = []
for i in range(len(strArray)):
    sortedPeople.append(strArray[i])

l = 0
for i in temp2:
    sortedPeople[l] = strArray[i]
    l += 1
#print("Sorted pEOPLE ARE ", sortedPeople)


for i in sortedPeople:
    if i not in dictionary.keys():
        finalOutput += i
        finalOutput += " "
    else:
        finalOutput += "- "

#print(sortedPeople)
# print(temp2)
# print(len(intArray), len(strArray), len(strArray)/2)
print(finalOutput.rstrip())