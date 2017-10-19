class Solution(object):
	phoneNumberDict = {'0':"",'1':"",'2':"abc",'3':"def",'4':"ghi",'5':"jkl",'6':"mno",'7':"pqrs",'8':"tuv",'9':"wxyz"}	

	def letterCombinations(self, digits):
		superList = []
		if not digits:
			return ""
		if(len(digits) > 1):
			temp = self.letterCombinations(digits[1:])
			for i in self.phoneNumberDict[digits[0]]:
				for j in range(len(temp)):
					temp2 = i + temp[j]
					superList.append(temp2)
			#print("SUPERLIST ",superList)
			return superList
		else:
			for m in self.phoneNumberDict[digits[0]]:
				superList.append(m)
			#print("SUPERLIST ",superList)
			return superList

variable=Solution()
output = variable.letterCombinations("9423")
print("output is ", output)


"""
test = ["ab","bc","cd"]
var = "a"
for i in range(len(test)):
	test[i] = var + test[i]
print(test)
"""
