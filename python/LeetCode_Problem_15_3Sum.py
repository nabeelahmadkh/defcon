class Solution(object):
	def threeSum(self, nums):
		outputList = []
		l =0
		for i in range(len(nums)):
			for j in range(len(nums)):
				for k in range(len(nums)):
					for p in range(len(nums)):
						if ((i != j) & (j != k) & (k != i)):
							if(nums[i]+nums[j]+nums[k]+nums[p] == 0):
								#print("nums ",nums[i],nums[j],nums[k])
								#print(" outputList1 ",outputList)
								flag = 0
								for m in outputList:
									temp = m[:]
									#print("m is ",m)
									if nums[i] in temp:
										temp.remove(nums[i])
										#print("temp 1",temp)
										if nums[j] in temp:
											temp.remove(nums[j])
											#print("temp 2",temp)
											if nums[k] in temp:
												temp.remove(nums[k])
												#print("temp 3",temp)
												flag = 1
												break
								#print(" outputList2 ",outputList)
								#print("temp flag",temp, flag)
								#print("nums ",nums[i],nums[j],nums[k])
								#`if((nums[i] == 0) & (nums[j] == 0) & (nums[k] == 0) & (nums[p] == 0)):
									#print("flag ", flag)
									#print("output list ",outputList)
								if flag == 0:
									if l == 0:
										outputList.append([nums[i],nums[j],nums[k],nums[p]])
										outputList.pop(0)
										#print("1")
									else:#
										outputList.append([nums[i],nums[j],nums[k],nums[p]])
										#print("1")
									l += 1
								#print(" outputList3 ",outputList)
		#print("outputList is ",outputList)
		return outputList
		
variable=Solution()
output = variable.threeSum([-4,-2,1,-5,-4,-4,4,-2,0,4,0,-2,3,1,-5,0])
print("output is ", output)