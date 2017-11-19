class Solution(object):
	def longestWord(self, words):
		sortedList = sorted(words, key=lambda x: len(x))
		longest = len(sortedList[len(sortedList) - 1])
		outputString = []
		print(" longest ",longest)
		for i in words:
			if len(i) == 1:
				output = self.recursiveFind(i, sortedList, long)
				print("output is ",output)
				outputString.append(output)
		print("outputString ",outputString)
		outputString = sorted(outputString, key=lambda x: len(x))
		print("outputString ",outputString)
		length = len(outputString[len(outputString) - 1])
		print("length ", length)
		print("outputString is ",outputString)
		return outputString[len(outputString) - 1]		


	def recursiveFind(self, prefix, listofwords, longest):
		#print("prefix is ",prefix)
		if len(prefix) > longest:
			print(" 2 ")
			return prefix
		flag = 0
		#print(listofwords)
		print(" prefix is ",prefix)
		output = ""
		for i in listofwords:
			if prefix == "appl":
				print(" i is ",i,prefix)
			if prefix == i[:-1]:
				print("prefix is ",prefix,i)
				output = self.recursiveFind(i, listofwords, longest)
				print(" output 2 is ",output)
				flag = 1
				if output != None:
					return output
		if flag == 0:
			return prefix


words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
variable = Solution()
output = variable.longestWord(words)
print("output of the program is ",output)