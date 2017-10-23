class Solution(object):
	def generateParenthesis(self, n):
		masterList = []
		output = self.generateParenthesis2(2*n)
		for i in output:
			temp = self.isValid(i)
			if temp == True:
				masterList.append(i)
		return masterList

	def generateParenthesis2(self, n):
		if n == 1:
			return ["(",")"]
		masterList = []
		combinations = self.generateParenthesis2(n-1)
		for i in range(len(combinations)):
			temp = "("+combinations[i]
			masterList.append(temp)
		for i in range(len(combinations)):
			temp = ")"+combinations[i]
			masterList.append(temp)
			
		return masterList
	
	def isValid(self, s):
		flag = ['']*10000
		check = 0
		k = 0
		if (len(s) == 1) or not s:
			return False
		for i in s:
			#print(" ",i)
			if (i == '(') or (i == '{') or (i == '['):
				#print("i flag k ",i,flag[k])
				flag[k] = i
				k += 1
				check = 1
			else:
				if flag[k-1] == '(':
					#print("i flag k ",i,flag[k])
					if i == ')':
						#print("i flag k ",i,flag[k])
						check = 0
						k -= 1
					else:
						return False
				elif flag[k-1] == '[':
					#print("i flag k ",i,flag[k])
					if i == ']':
						#print("i flag k ",i,flag[k])
						check = 0
						k -= 1
					else:
						return False
				elif flag[k-1] == '{':
					#print("i flag k ",i,flag[k])
					if i == '}':
						#print("i flag k ",i,flag[k])
						check = 0
						k -= 1
					else:
						return False
				else:
					return False
		if k == 0:
			return True
		else: 
			return False

variable = Solution()
output = variable.generateParenthesis(3)
print("output of the program is ",output)