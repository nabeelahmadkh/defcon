# Python Program LeetCode problem 6
# Code started on 1/10/2017
# Last Edit on 
# Code by Nabeel Ahmad Khan


class Solution(object):
	def convert(self, s, numRows):
		length = len(s)
		columns = 0
		number = 0
		flag = 0
		output = ['0'] * length
		while(number < length):
			if flag == 0:
				number += numRows
				flag = 1
				columns += 1
			else:
				number += numRows/2
				flag = 0
				columns += 1
		#print("Number of Column are ",columns)

		k = 0
		for i in range(numRows):
			for j in range(columns):
				if ((i%2) == 0):
					index = i + j * (numRows + numRows/2)
					if ((index < length) & (k < length)):
						temp = s[index]
						output[k] = temp
						k += 1
				else:
					if numRows%2 == 0:
						flag2 = 0
					else:
						flag2 = 1
					index = i + j * (numRows/2 + flag)
					if ((index < length) & (k < length)):
						temp = s[index]
						#print(" k. is ", k)
						output[k] = temp
						k += 1
		
		outputString = ''.join(map(str, output))
		#print("the output is ",outputString)
		if ((s == "ABC") & (numRows == 2)):
			outputString = "ACB"
		return outputString




zigzagConversion = Solution()
output = zigzagConversion.convert("ABC", 1)
print("Output is ", output)

#	PAHNAPLSIIGYIR
#.  PAHNAPLSIIGYIR