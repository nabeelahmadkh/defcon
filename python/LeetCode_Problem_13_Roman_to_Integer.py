class Solution(object):
	def romanToInt(self, s):
		length = len(s)
		numberLevel1 =  {"I":1,"II":2,"III":3,"IV":4,"V":5,"VI":6,"VII":7,"VIII":8,"IX":9}
		numberLevel2 =  {1:"X",2:"XX",3:"XXX",4:"XL",5:"L",6:"LX",7:"LXX",8:"LXXX",9:"XC"}
		numberLevel3 =  {1:"C",2:"CC",3:"CCC",4:"CD",5:"D",6:"DC",7:"DCC",8:"DCCC",9:"CM"}
		numberLevel4 =  {1:"M",2:"MM",3:"MMM"}
		numList = map(str, str(s)) 
		print("numList length",numList,length)
		i = length - 1
		print("numberLevel ",numberLevel1["IV"])
		temp = ""
		while numList > 0:

					

		
variable = Solution()
number = "xx"

output = variable.romanToInt(number)
print("the output is ",output)