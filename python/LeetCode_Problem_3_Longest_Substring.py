# Python Program LeetCode problem 3 Substring using Brute Force
# Code started on 08/08/2017
# Last Edit on 09/08/2017
# Code by Nabeel Ahmad Khan
# Algorithm used is Brute Force (Better Algorithm is Hashing - O(n) complexity can be achieved using Hashset)


class Solution(object):
    def lengthOfLongestSubstring(self, s):
    	tempList = []
    	finalList = []
    	stringLength = len(s) - 1
    	j = 0
    	subStringLength = 0
    	for i in s:
    		if j > 0:
    			tempVariable = j - 1
    			flag = 0
    			while tempVariable >= 0:
    				if i == tempList[tempVariable]:
    					flag = 1
    					break
    				tempVariable -= 1
    			if flag != 1:
    				tempList.append(i)
    				j += 1

    			else:
    				if len(tempList) >= subStringLength:
						subStringLength = len(tempList)
						finalList = tempList
						tempList = [i]	#make templist empty 
						j = 1
						continue


    		else :
    			tempList.append(i)
    			j += 1

		if len(tempList) >= subStringLength:
			subStringLength = len(tempList)
			finalList = tempList
    	print "the substring is ", finalList
    	print "length ",len(finalList)


variable = Solution()
#	Enter the string to be evaluated
string = str(raw_input())

print "The string entered is ", string

variable.lengthOfLongestSubstring(string)