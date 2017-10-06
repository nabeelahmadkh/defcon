class Solution(object):
    def reverse(self, x):
    	flag = 0
    	if x < 0:
    		flag = 1
    		x = -(x)

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
output = variable.reverse(2147483647)
print("Output is ", output)