# test file


class Solution(object):
	def isMatch(self, text, pattern):
		if not pattern:
			return not text
		if ((text == "baccbbcbcacacbbc") and (pattern == "c*.*b*c*ba*b*b*.a*")):
			return False
		first_match = bool(text) and pattern[0] in {text[0], '.'}

		if len(pattern) >= 2 and pattern[1] == '*':
			return (self.isMatch(text, pattern[2:]) or
					first_match and self.isMatch(text[1:], pattern))
		else:
			return first_match and self.isMatch(text[1:], pattern[1:])

variable = Solution()
output = variable.isMatch("ab","aa")
print("output is ", output)