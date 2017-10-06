# Python Program LeetCode problem 10
# Code started on 1/10/2017
# Last Edit on 
# Code by Nabeel Ahmad Khan

class Solution(object):
	def isMatch(self, s, p):
		flag = False
		checkList = map(str, str(s))
		regexp = map(str, str(p))
		print("checkList regexp ",checkList[0],regexp)
		length1 = len(s)
		length2 = len(p)
		print("length ", length1,length2)
		i = 0
		j = 0
		while(j<length2):
			if((regexp[j] == '.') | (regexp[j] =='*')):
				print("1")
				if(regexp[j] == '.'):
					if((j+1) < length2):
						if(regexp[j+1] == '*'):
							temp = checkList[i+1]
							i += 1
							while((temp == checkList[i]) & (i<length1)):
								i += 1
								if(i >= length1):
									break	
							j += 2
							if(i >= length1):
								break
							
						else:
							i += 1
							j += 1
					else:
						i += 1
						j += 1
			
			else:
				if((j+1) < length2):
					print("2")
					print("i j 5",i,j)
					if(regexp[j+1] == '*'):
						temp = regexp[j]
						flag2 = 0
						print("i j 6",i,j)
						while ((temp == checkList[i]) & (i<length1)):
							i += 1
							flag2 = 1
							print("i j 1",i,j)
							if(i >= length1):
								break	

						j += 2
						if((flag == 1) & (j < length2)):
							if(checkList[i-1] == regexp[j]):
								j += 1
						if((i >= length1) & (j < length2)):
							if(checkList[i-1] == regexp[j]):
								j += 1

						print("i j 2",i,j)
						if(i >= length1):
								break
					else:
						if(checkList[i] == regexp[j]):
							print("i j 3",i,j)
							i += 1
							j += 1
				else:
					if((i < length1) * (j< length2)):
						if(checkList[i] == regexp[j]):
							print("i j 4",i,j)
							i += 1
							j += 1
					else:
						j += 1

		print(" i j ", i,j)
		if((i >= length1) & (j >= length2)):
			flag =True
		

		return flag

variable=Solution()
output = variable.isMatch("aaa", "ab*a*c*a")
print("output is ", output)
