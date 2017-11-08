

class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution(object):
	def swapPairs(self, head):
	    pre, pre.next = self, head
	    while pre.next and pre.next.next:
	        a = pre.next
	        b = a.next
	        pre.next, b.next, a.next = b, a, b.next
	        pre = a
	    return self.next

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
#addNode1(11)
#addNode1(13)
display1()

variable = Solution()
output = variable.swapPairs(start1)

while(output.next != None):
	print(output.val)
	output = output.next
print(output.val)
