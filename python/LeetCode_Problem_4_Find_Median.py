# Python Program LeetCode problem 4 
# Code started on 28/08/2017
# Last Edit on 29/08/2017
# Code by Nabeel Ahmad Khan


class Solution():
	def calculateMedian(self, a, b):
		lengthOfFirstList = len(a)
		lengthOfSecondList = len(b)
		finalList = []
		i = j = k =0
		while i<lengthOfFirstList or j<lengthOfSecondList:
			if i == lengthOfFirstList:
				finalList.append(b[j])
				j+=1
				k+=1
				continue

			if j == lengthOfSecondList:
				finalList.append(a[i])
				i+=1
				k+=1
				continue

			if a[i] > b[j]:
				finalList.append(b[j])
				j+=1
				k+=1

			else:
				finalList.append(a[i])
				i+=1
				k+=1

		print "The final string is"
		print finalList
		lengthOfThirdList = len(finalList)
		if lengthOfThirdList%2 == 0:
			median = (finalList[lengthOfThirdList/2]+finalList[(lengthOfThirdList/2)-1])/2
			print "The even median is ",median
		else:
			median = finalList[(lengthOfThirdList/2)]
			print "The median is ",median


var = Solution()

firstList = [1, 3, 6]
secondList = [4, 5, 7]

var.calculateMedian(firstList, secondList)
