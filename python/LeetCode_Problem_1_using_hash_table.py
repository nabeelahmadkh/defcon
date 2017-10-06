# Python Program LeetCode problem 1 usign hash table.
# Code started on 08/08/2017
# Last Edit on 09/08/2017
# Code by Nabeel Ahmad Khan
# Algorithm used is Hashing.
# (temp != nums[i])

class Solution(object):
	def twoSum(self, nums, target):
		flag = [0, 0]
		nextflag = 0
		numsHash = [0] * 100000
		for i in nums:
			tempHash = hash(i)
			numsHash[tempHash] += 1
			#print("i is  ", i)


		for i in range(len(nums)):	# i is using as an Index because we are using len() function on a List
			#print " first "
			temp = target - nums[i]
			if (numsHash[temp] >= 1):
				#print "Number found"
				#print("i is  temp num[i]",i,temp,nums[i])
				if(temp == nums[i]):
					if (numsHash[temp] > 1):
						nextflag = 1
						break
				else:
					break
		
		for j in range(len(nums)):
			if temp == nums[j]:
				if(nextflag == 0):
					return [i, j]	# using return statement here because Break will not bring it out from 2 loops.
				else:
					nextflag = 0

# Dont use the below code while submitting code on LeetCode.


var = Solution()	# Creating an Object for the Class.
nums = []

#input the numbers list and target
count = int(raw_input("Enter the count of numbers you want to enter in the list"))
print("Enter the Numbers")
for i in range(count):
	temp = int(raw_input())
	nums.append(temp)
#	tempHash = hash(temp)
#	print "Hash of the number entered is", tempHash
#	numsHash[tempHash] = 1

print "Enter the target"
target = int(raw_input())

print "The numbers you entered are "
	
for i in nums:
	print i

print "Target you entered is ",target

flag = var.twoSum(nums, target)	# Calling the sum Function. 
print flag
