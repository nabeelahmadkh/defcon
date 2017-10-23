class Solution(object):
	def threeSum(self, nums):
		outputList = []
		numsDict = {i:i for i in nums}
		flag = 0
		if len(nums)<3:
			return []
		#print("Dictionary is ",numsDict)
		for i in range(len(nums)):
			for j in range(len(nums)):
				flag = 0
				count = 2
				if i != j:
					rSum = -(nums[i] + nums[j])
					#print("rSum is ",rSum)
					if (rSum in numsDict.values()):
						if rSum in [nums[i],nums[j]]:
							if (rSum == nums[i]) & (rSum == nums[j]):
								count = nums.count(rSum)
								if count == 2:
									count -= 1
								#print([nums[i],nums[j],rSum],count)
							else:
								count = nums.count(rSum)
						if (not outputList) and count > 1:
							#print([nums[i],nums[j],rSum])
							outputList.append([nums[i],nums[j],rSum])

						else:
							for m in outputList:
								#print("m is ",m)
								#print("else ",[nums[i],nums[j],rSum])
								if (nums[i] in m) & (nums[j] in m) & (rSum in m):
									#print("append ",[nums[i],nums[j],rSum])
									flag = 1

							if (flag == 0) & (count > 1):
								outputList.append([nums[i],nums[j],rSum])
							if (rSum == 0) and (count >= 3):
								#print(" eneted")
								if not [nums[i],nums[j],rSum] in outputList:
									outputList.append([nums[i],nums[j],rSum])
		if len(outputList) == 1:
			if (outputList[0] == [-1,0,1]):
				return [[-1,0,1]]
		return outputList
		
variable=Solution()
output = variable.threeSum([-4,-2,1,-5,-4,-4,4,-2,0,4,0,-2,3,1,-5,0])
print("output is ", output)