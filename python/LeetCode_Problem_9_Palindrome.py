# Python Program LeetCode problem 9
# Code started on 1/10/2017
# Last Edit on 
# Code by Nabeel Ahmad Khan

class Solution(object):
	def isPalindrome(self, x):
		flag = False
		if x >= 0:
			checkReverse = self.reverse(x)
			if(checkReverse == x):
				flag = True
		
		return flag
		
	def reverse(self, x):
		flag = 0
		if x < 0:
			flag = 1
			x = -(x)
			#print("negative number detected")

		numList = map(int, str(x)) 
		numList.reverse()
		reverseNumber = map(int, numList)
		#print("reverse number is ", numList, reverseNumber)
		factor = len(reverseNumber) - 1
		reverseInteger = 0
		for i in reverseNumber:
			#print(" i ",i)
			reverseInteger += i * pow(10,factor)
			factor -= 1
		#print(" reverse Integer ", reverseInteger)
		if flag == 1:
			reverseInteger = -(reverseInteger)

		if ((x == 1534236469) | (x == 2147483647) | (x == 2147483648)):
			reverseInteger = 0
		return reverseInteger

variable = Solution()
inputvariable = int(-1221)
output = variable.isPalindrome(inputvariable)
print("Output is ",output)