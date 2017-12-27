#!/bin/python
def insertionSort(ar):
    m = len(ar)
    m -= 1
    temp = ar[m]
    m -= 1
    count = 0
    while(m>=0):
        if ar[m]>temp:
            if m == 0:
                ar[m+1] = ar[m]
                for i in ar:
                    print i,
                print
                ar[m] = temp
                for i in ar:
                    print i,
                print
                break
            else:
                ar[m+1] = ar[m]
                for i in ar:
                    print i,
                print
        else:
            if count == 0:
                ar[m+1] = temp
            else:
                ar[m+1] = temp
                for i in ar:
                    print i,
                #print("\n")
            break
        count += 1
        m -= 1


    return ""

m = input()
ar = [int(i) for i in raw_input().strip().split()]
insertionSort(ar)
#print(m, ar)2 3 4 5 6 7 8 9 10 10
# 2 3 4 5 6 7 8 9 9 10
# 2 3 4 5 6 7 8 8 9 10
# 2 3 4 5 6 7 7 8 9 10
# 2 3 4 5 6 6 7 8 9 10
# 2 3 4 5 5 6 7 8 9 10
# 2 3 4 4 5 6 7 8 9 10
# 2 3 3 4 5 6 7 8 9 10
# 2 2 3 4 5 6 7 8 9 10
# 1 2 3 4 5 6 7 8 9 10