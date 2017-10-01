# Python Program LeetCode problem 
# Code started on 30/09/2017
# Last Edit on 30/09/2017
# Code by Nabeel Ahmad Khan
# Algorithm used is of the Order(n)


class Solution(object):
	def longestPalindrome(self, s):
		stringLength = len(s)
		stack = []
		pointer = 0
		flag = 0
		frontPointer = 0
		backPointer = 0
		length = 1
		longestLength = 1
		longestLengthIndex = -1
		#print("The length of string is ", stringLength)
		for i in s:
			#print("1")
			frontPointer = pointer + 1
			backPointer = pointer - 1
			while((backPointer >= 0) & (frontPointer <= (stringLength - 1))):
				#print("2")
				#print("frontPointer ",frontPointer)
				#print("backPointer ",backPointer)
				if (s[backPointer] == s[frontPointer]):
					#print(s[backPointer],s[frontPointer])
					#print("3")
					length += 2
					if (length > longestLength):
						#print("4")
						longestLength = length
						longestLengthIndex = pointer
					backPointer -= 1
					frontPointer += 1
				else:
					break

			pointer += 1
			length = 1
		#print("The longest length is ",longestLength," at position ",(longestLengthIndex - longestLength/2))

		length = 0
		pointer = 0
		for i in s:
			#print("1")
			frontPointer = pointer + 1
			backPointer = pointer
			while((backPointer >= 0) & (frontPointer <= (stringLength - 1))):
				#print("2")
				#print("frontPointer ",frontPointer)
				#print("backPointer ",backPointer)
				if (s[backPointer] == s[frontPointer]):
					#print(s[backPointer],s[frontPointer])
					#print("3")
					length += 2
					#print("length is ",length)
					if (length > longestLength):
						#print("4")
						longestLength = length
						flag = 1
						#print("Longest Length is ",longestLength)
						longestLengthIndex = pointer
					backPointer -= 1
					frontPointer += 1
				else:
					break

			pointer += 1
			length = 0
		#print("The longest length is ",longestLength," at position ",(longestLengthIndex - longestLength/2 + 1))

		#print("longestLengthIndex ",longestLengthIndex," longestLength ",longestLength," flag ", flag)
		if flag == 0:
			end = longestLengthIndex + longestLength/2
			start = (longestLengthIndex - longestLength/2)
		else:
			end = longestLengthIndex + longestLength/2
			start = (longestLengthIndex - longestLength/2 + 1)

		#print("start ",start," end ",end)
		#print(s[6:8])
		end = end+1
		output = s[start:end]

		if stringLength == 1:
			output = s
		if not output:
			output = s[0]
		return output

		
palindromeChecker = Solution()
palindromeString = "abcda"
output = palindromeChecker.longestPalindrome(palindromeString)
print("longest palindrome is ",output)
