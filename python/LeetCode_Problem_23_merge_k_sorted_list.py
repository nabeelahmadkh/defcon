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

class UnorderedList:
    def __init__(self):
        self.start = None
        self.last = None

    def add(self,item):
        temp = ListNode(item)
        if self.start == None:
            self.start = temp
            self.last = temp
            temp.next = None
            return
        self.last.next = temp
        self.last = temp
        
    def display(self):
        current = self.start
        while current != None:
            print current.val
            current = current.getNext()

class Solution(object):
	def mergeKLists(self, lists):
		myLinkedList3 = UnorderedList()
		print("number of lists are ",len(lists))
		for i in range(len(lists)):
			temp = lists[0].value
			while(k < len(lists)):
				if temp < lists[k].val:
					temp = lists[k].val


myLinkedList1 = UnorderedList()
myLinkedList1.add(2)
myLinkedList1.add(6)
myLinkedList1.add(7)
myLinkedList1.add(8)

myLinkedList2 = UnorderedList()
myLinkedList2.add(1)
myLinkedList2.add(2)
myLinkedList2.add(3)
myLinkedList2.add(2)
myLinkedList2.add(6)

variable = Solution()
output = variable.mergeKLists([myLinkedList1.start, myLinkedList2.start])
print("output of the program is ",output)



