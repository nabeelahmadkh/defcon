# Python Program LeetCode problem 1 usign hash table.
# Code started on 08/08/2017
# Last Edit on 09/08/2017
# Code by Nabeel Ahmad Khan
# Algorithm used is Hashing.

class Solution(object):
	def twoSum(self, nums, target, numsHash):
		flag = [0, 0]
		for i in range(len(nums)):	# i is using as an Index because we are using len() function on a List
			print " first "
			temp = target - nums[i]
			if (numsHash[temp] == 1):
				print "Number found"
				break
		for j in range(len(nums)):
			if temp == nums[j]:
				return [i+1, j+1]	# using return statement here because Break will not bring it out from 2 loops.


# Dont use the below code while submitting code on LeetCode.


var = Solution()	# Creating an Object for the Class.
numsHash = [None] * 100000000	# Hashed Array.
nums = []

#input the numbers list and target
count = int(raw_input("Enter the count of numbers you want to enter in the list"))
for i in range(count):
	temp = int(raw_input())
	nums.append(temp)
	tempHash = hash(temp)
	print "Hash of the number entered is", tempHash
	numsHash[tempHash] = 1

print "Enter the target"
target = int(raw_input())

print "The numbers you entered are "
	
for i in nums:
	print i

print "Target you entered is ",target

flag = var.twoSum(nums, target, numsHash)	# Calling the sum Function. 
print flag
