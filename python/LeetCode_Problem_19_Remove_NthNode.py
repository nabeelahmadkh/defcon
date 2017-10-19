class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

	def getNext(self):
		return self.next

	def setNext(self, newnext):
		self.next = newnext
		
	def getData(self):
		return self.val
		
	def setData(self, newdata):
		self.val = newdata

def add(item):
	temp = ListNode(item)
	global start 
	global last
	if start == None:
		start = temp
		last = temp
		temp.next = None
		return
	last.next = temp
	last = temp
		
def display():
	global start 
	global last
	current = start
	while current != None:
		print current.val
		current = current.getNext()
   

class Solution(object):
	def removeNthFromEnd(self, head, n):
		global start 
		global last 
		count = 0
		localStart = start
		localPointer = start
		#print("localStart localPointer",localStart.val,localPointer.val)
		while(localPointer.next != None):
			localPointer = localPointer.next
			if count >= n:
				localStart = localStart.next
			count += 1
		
		#print("localStart localPointer",localStart.val,localPointer.val)
		
		if count < n:
			return []
		elif count == n:
			temp = localStart.next
			localStart.next = temp.next
			return [localStart.val]
		else:
			temp = localStart.next
			localStart.next = temp.next
			return temp.val

start = None 
last = None
add(2)
add(1)
add(3)
add(4)

display()
variable = Solution()
output = variable.removeNthFromEnd(start,2)
print("output of the program is ",output)
display()




