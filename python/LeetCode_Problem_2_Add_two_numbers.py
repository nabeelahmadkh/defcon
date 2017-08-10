# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

class ListNode:
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
		self.head = None

	def add(self,item):
		temp = ListNode(item)
		temp.setNext(self.head)
		self.head = temp

	def display(self):
		current = self.head
		while current != None:
			print current.val
			current = current.getNext()


print "Creating a Linked List"

myLinkedList = UnorderedList()
myLinkedList.add(50)
myLinkedList.add(60)
myLinkedList.add(70)

print "the linked list entered is"
myLinkedList.display()






