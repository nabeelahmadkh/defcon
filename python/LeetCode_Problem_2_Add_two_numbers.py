# Python Program LeetCode problem 2 usign Linked List.
# Code started on 11/08/2017
# Last Edit on 12/08/2017
# Code by Nabeel Ahmad Khan


class Solution(object):     
    def addTwoNumbers(self, l1, l2):    # function for calculating SUM of two linked list 
        print "Entered"

        #creating a list from the Linked List so as to perform the addition operation 
        arr1 = []
        arr2 = []
        arr3 = []
        temp1 = l1.start
        temp2 = l2.start
        while temp1 != None:
            arr1.append(int(temp1.getData()))
            temp1 = temp1.getNext()
        print arr1
        while temp2 != None:
            arr2.append(int(temp2.getData()))
            temp2 = temp2.getNext()
        print arr2

        print "length of arr1 is ",len(arr1)
        print "length of arr2 is ",len(arr2)

        counter1 = len(arr1) - 1
        counter2 = len(arr2) - 1
        if counter2 > counter1:
            max = counter2
        else:
            max = counter1

        #adding the two List.

        carry = 0
        while counter1 >= 0 or counter2 >=0:
            if counter1 < 0:
                arr1[counter1] = 0
            if counter2 < 0:
                arr2[counter2] = 0
            temp3 = arr1[counter1] + arr2[counter2] + carry
            print " 3 values ",carry,arr1[counter1],arr2[counter2]
            if temp3 >= 10:
                carry = 1
                temp3 = temp3 % 10
            else:
                carry = 0
            arr3.append(temp3)
            counter2 = counter2 - 1
            counter1 = counter1 - 1
        arr3 = arr3[::-1]           # used for reversing a list
        print "the sum calculated is ", arr3    # Displaying the sum of two list 

        #making Linked List from List again.
        myLinkedList3 = UnorderedList()
        counter3 = len(arr3)

        i = 0
        while i < counter3:
            myLinkedList3.add(arr3[i])
            print " 23 "
            i = i + 1

        print "The two linked list are "
        print myLinkedList3.display()


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


print "First Linked List is"
myLinkedList1.display()

print "Second Linked List  is"
myLinkedList2.display()

addSolution = Solution()
addSolution.addTwoNumbers(myLinkedList1, myLinkedList2)



