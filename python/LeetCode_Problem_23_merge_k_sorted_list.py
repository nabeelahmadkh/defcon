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
		newlist = []
		check = 0
		count = 0
		for o in range(len(lists)):
			temp = lists[o]
			while(temp.next != None):
				count += 1
				temp = temp.next
			count += 1
		print("the value of count is ",count)
		#print("number of lists are ",len(lists))
		for i in range(count):
			for l in range(len(lists)):
				if lists[l] != None:
					temp = lists[l].val
					check = l
					break
			k = 0
			#print("entered 1")
			while(k < len(lists)):
				#print("entered 2")
				if lists[k]:
					#print("entered 3")
					print("temp lists[k]", temp, lists[k].val)
					if temp > lists[k].val:
						#print("entered 4")
						temp = lists[k].val
						check = k
				k += 1
			newlist.append(temp)
			print("check is ",check)
			if lists[check] != None:
				lists[check] = lists[check].next
		print("the new list is ", newlist)
		myLinkedList5 = UnorderedList()
		for i in range(count):
			myLinkedList5.add(newlist[i])
		return myLinkedList5





myLinkedList1 = UnorderedList()
myLinkedList1.add(2)
myLinkedList1.add(6)
myLinkedList1.add(7)
myLinkedList1.add(9)

myLinkedList2 = UnorderedList()
myLinkedList2.add(1)
myLinkedList2.add(2)
myLinkedList2.add(4)

myLinkedList4 = UnorderedList()
myLinkedList4.add(3)
myLinkedList4.add(11)

variable = Solution()
output = variable.mergeKLists([myLinkedList1.start, myLinkedList2.start, myLinkedList4.start])
print("output of the program is ",output.display())



