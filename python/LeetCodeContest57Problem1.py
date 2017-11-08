class Solution(object):
	def longestWord(self, words):
		if words != None:
			#arr = [1000] * None
			sortedList = sorted(words, key=lambda x: len(x))
			print(sortedList)
			longestString = sortedList[0]
			flag = 1
			i = 0
			j = 0
			while(i < len(sortedList)):
				if flag == 1:
					flag = 0
					pass
				else:
					j = i
					length = len(sortedList[i])
					temp2 = longestString
					smallest = sortedList[j][len(sortedList[j]) - 1]
					#print("smallest ",smallest)
					
					while(len(sortedList[j]) == length):
						temp = sortedList[j][:-1]
						#print(" 3 ",sortedList[j],temp)
						if temp == temp2:
							#print(" 4 ")
							if ord(smallest) >= ord(sortedList[j][len(sortedList[j]) - 1]):
								#print(" 1 ",ord(smallest),ord(sortedList[j][len(sortedList[j]) - 1]))
								longestString = sortedList[j]

						j += 1
						if j == len(words):
							#print("2")
							break
						else:
							continue
				i = j
			#print("longest string ",longestString)
			return longestString
		else:
			return None


words = ["m","mo","moc","moch","mocha","l","la","lat","latt","latte","c","ca","cat"]
variable = Solution()
output = variable.longestWord(words)
print("output of the program is ",output)