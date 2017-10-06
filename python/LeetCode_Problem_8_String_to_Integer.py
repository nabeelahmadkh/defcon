class Solution(object):
	def myAtoi(self, str):
		
		for i in str:
			print("value in i is ", ord(i))
		print("String enetered is ", str)
		#print("Number is ", number)



variable = Solution()
str = "nabeel"
output = variable.myAtoi(str)
print("the output is", output)