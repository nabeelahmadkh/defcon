# Python Program for HackerRank Problem Pat.
# Code started on 11/02/2015
# Last Edit on 07/08/2017
# Code by Nabeel Ahmad Khan


def check(arr):
    flag=0
    l=len(arr)

    if l==2:
        if arr[0]==arr[1]:
            return False
        else:
            return True
    if arr[1]>=arr[0] or arr[l-1]<=arr[l-2]:
        return False
    else:
        for i in range(2,l):
            if arr[i]<arr[i-1]:
                flag=1
            else:
                j=i
                break
        for i in range(j,l-1):
            if arr[i+1]>arr[i]:
                flag=1
            else:
                return False

    if flag==1:
        return True


n=int(raw_input())
arr=[int(i) for i in raw_input().split()]

if check(arr):
    print 'Yes'
else:
    print 'No'
