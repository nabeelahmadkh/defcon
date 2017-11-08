
#Definition for singly-linked list.
class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution(object):
	def swapPairs(self, head):
		start1 = head
		print(head.val)
		if ((head != None) & (head.next != None)):
			temp = None
			temp1 = start1
			temp2 = temp1.next
			while(temp1 != None):
				if(temp1 == start1):
					#print(temp1.val,temp2.val)
					#print("__1__")
					start1 = temp2
					temp1.next = temp2.next
					temp2.next = temp1
				else:
					#print(temp.val,temp1.val, temp2.val)
					#print("__2__")
					temp.next = temp2
					temp1.next = temp2.next
					temp2.next = temp1
				temp = temp1
				if temp1.next != None:	
					#print("__3__")
					temp1 = temp1.next
					#print(temp1.val,temp1.next)	
					if temp1.next != None:
						temp2 = temp1.next
						print(temp2.val,temp2.next)
						print(start1.val)
					else:
						temp1 = None
				else:
					#print("__4__")
					temp1 = None
			return start1
		else: 
			return start1


		"""
		:type head: ListNode
		:rtype: ListNode
		"""

def display1():
	global start1,end1
	start = start1
	while(start.next != None):
		print(start.val)
		start = start.next
	print(start.val)
	print("end")

def addNode1(value):
	global start1, end1
	if start1 == None:
		start1 = ListNode(value)
		end1 = start1
	else:
		end1.next = ListNode(value)
		end1 = end1.next



start1 = None
last1 = None
addNode1(1)
addNode1(5)
addNode1(9)
addNode1(11)
#addNode1(13)
display1()

variable = Solution()
variable.swapPairs(start1)

display1()




