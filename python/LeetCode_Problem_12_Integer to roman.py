class Solution(object):
	def intToRoman(self, num):
		output = ""
		numberLevel1 =  {1:"I",2:"II",3:"III",4:"IV",5:"V",6:"VI",7:"VII",8:"VIII",9:"IX"}
		numberLevel2 =  {1:"X",2:"XX",3:"XXX",4:"XL",5:"L",6:"LX",7:"LXX",8:"LXXX",9:"XC"}
		numberLevel3 =  {1:"C",2:"CC",3:"CCC",4:"CD",5:"D",6:"DC",7:"DCC",8:"DCCC",9:"CM"}
		numberLevel4 =  {1:"M",2:"MM",3:"MMM"}
		
		dividend = num
		i = 1
		while dividend != 0:
			temp = dividend%10
			if temp != 0:
				if i == 1:
					output = numberLevel1[temp]+output
				elif i == 2:
					output = numberLevel2[temp]+output
				elif i == 3:
					output = numberLevel3[temp]+output
				else:
					output = numberLevel4[temp]+output
			i += 1
			dividend = dividend/10
			#print("temp dividend numberLevel1",temp, dividend,numberLevel1[temp])
		return output

variable = Solution()
number = 1466

output = variable.intToRoman(number)
print("the output is ",output)
