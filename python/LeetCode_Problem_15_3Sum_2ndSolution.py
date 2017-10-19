solutionarray = []


class Solution(object):
	def threeSum(self, nums):
		target = 0
		output = split(nums, target)
		return output

		
def split(arrayNum, target):
	output = []
	newtarget = target - arrayNum[0]
	#print("arrayNum  ",arrayNum)
	if len(arrayNum) > 1:
		for i in  range(len(arrayNum) - 1):
			temp = i+1
			subarrayNum = arrayNum[temp:]
			temp = split(subarrayNum, newtarget)
			sum = 0
			for k in temp:
				sum += k
			sum += arrayNum[0]
			print("sum target",sum,target)
			if sum == target:
				for l in range(len(temp)):
					output.append(temp[l])
					print(" addition ",temp[l])
				solutionarray.append(output)
				print("target ",target)
		#print("output",output)
		for i in range(len(output)):
			output[i] = arrayNum[0] + output[i]
		return output
	else:
		#print("last ",arrayNum)
		return arrayNum

variable = Solution()
output = variable.threeSum([-4,-2,1,-5,-1,-7,10])
print("output is ", solutionarray)