class Solution(object):
	def longestCommonPrefix(self, strs):
		if not strs:
			return ""
		longestSubs = strs[0]
		longestSubsLength = len(longestSubs)
		for i in strs:
			temp = ""
			k = 0
			for j in i:
				if (k < (len(longestSubs))):
					if j == longestSubs[k]:
						temp = temp+j
						k += 1
					else:
						break
				else:
					break
			if len(temp) < len(longestSubs):
				longestSubs = temp
		#("temp longestSubs = ",temp,longestSubs)
		return longestSubs

variable=Solution()
output = variable.longestCommonPrefix([])
print("output is ", output)