class Solution(object):
	def isValid(self, s):
		flag = ['']*10000
		check = 0
		k = 0
		if (len(s) == 1) or not s:
			return False
		for i in s:
			#print(" ",i)
			if (i == '(') or (i == '{') or (i == '['):
				print("i flag k ",i,flag[k])
				flag[k] = i
				k += 1
				check = 1
			else:
				if flag[k-1] == '(':
					print("i flag k ",i,flag[k])
					if i == ')':
						print("i flag k ",i,flag[k])
						check = 0
						k -= 1
					else:
						return False
				elif flag[k-1] == '[':
					print("i flag k ",i,flag[k])
					if i == ']':
						print("i flag k ",i,flag[k])
						check = 0
						k -= 1
					else:
						return False
				elif flag[k-1] == '{':
					print("i flag k ",i,flag[k])
					if i == '}':
						print("i flag k ",i,flag[k])
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
output = variable.isValid("((")
print("output of the program is ",output)
		
		