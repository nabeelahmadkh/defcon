# Python Program LeetCode problem 1 .
# Code started on 08/08/2017
# Last Edit on 09/08/2017
# Code by Nabeel Ahmad Khan
# Algorithm used is Brute Force.

class Solution(object):
	def twoSum(self, nums, target):
		flag = [0, 0]
		for i in range(len(nums)):	# i is using as an Index because we are using len() function on a List
			for j in range(len(nums)):
				print " first "
				if (i != j):
					print " nums[i] nums[j] ",nums[i],nums[j]
					temp = int(nums[i]) + int(nums[j])
					print " second  target = ",temp
					if (temp == target):
						print "variable found at",i+1,j+1
						flag = [i+1, j+1]
						return flag	# using return statement here because Break will not bring it out from 2 loops.


# Dont use the below code while submitting code on LeetCode 


var = Solution()	# Creating an Object for the Class
nums = []

#input the numbers list and target 
count = int(raw_input("Enter the count of numbers you want to enter in the list"))
for i in range(count):
	nums.append(raw_input())

print "Enter the target"
target = int(raw_input())

print "The numbers you entered are "
	
for i in nums:
	print i

print "Target you entered is ",target

flag = var.twoSum(nums, target)	# Calling the sum Function. 
print flag
