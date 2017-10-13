class Solution(object):
	def threeSum(self, nums):
		outputList = [[]]
		l =0
		for i in range(len(nums)):
			for j in range(len(nums)):
				for k in range(len(nums)):
					if (i != j & j != k & k != i):
						#print(nums[i],nums[j],nums[k])
						if(nums[i]+nums[j]+nums[k] == 0):
							outputList.append([nums[i],nums[j],nums[k]])
							l += 1
		return outputList
					
		"""
		:type nums: List[int]
		:rtype: List[List[int]]
		"""
		
variable=Solution()
output = variable.threeSum([1,-1,0,2,3])
print("output is ", output)