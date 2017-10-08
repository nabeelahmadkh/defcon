import numpy as np

class Solution(object):
	def maxArea(self, height):
		length = len(height)
		print("length of the list is ", length)
		max1 = 0
		max2 = 0
		#maxarea = np.empty([100, 100], dtype=int)
		maxA = 0
		pointer1 = 0
		pointer2 = length - 1
		while pointer1 < pointer2:
			if height[pointer1]<height[pointer2]:
				smallHeight = height[pointer1]
			else:
				smallHeight = height[pointer2]
			temp = smallHeight * (pointer2 - pointer1)
			if maxA < temp:
				maxA = temp
			if height[pointer1] < height[pointer2]:
				pointer1 += 1
			else:
				pointer2 -= 1

		print("value of maxA is", maxA)
		return maxA

variable = Solution()
output = variable.maxArea([1,2,3,4])
print("the output is ", output)