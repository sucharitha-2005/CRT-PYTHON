class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class singlelinkedlist:
    def __init__(self ):
        self.head = None
        self.tail = None
        self.size = 0
    def insertAtstart(self,val):
        newNode = Node(val)   
        if self.head is None:
            self.head = self.tail = newNode
            self.size += 1
            return
        newNode.next = self.head
        self.head = newNode
        self.size += 1
        return head
def insertAtEnd(self, val):
    newNode = Node(val)
    if self.head is None:
        self.head = self.tail = newNode
        self.size += 1
        return
    self.tail.next = newNode
    self.tail = newNode
    return head
def insertAtEnd(self, val):
    newNode = Node(val)
    if self.head is None:
        self.head = newNode
        self.size + = 1
        return
    curr = self.head
    while curr.next:
        curr =  curr.next
    self.size += 1
    curr.next = newNode
    return head
def delAtStart(self):
    if self.head is None:
        return -1
    if self.head.next is None:
        self.head = None
        return
    temp = self.head
    self.head = self.head.next
    temp.next = None
    return self.head
def delAtEnd(self):
    if self.head.next is None
        


def display(self):
    curr = self.head
    while curr:
        print(curr.data)
        curr = curr.next
def deleteAtIndex(self,Index):
    if self.head is None
        return -1
    if index==0:
        deleteAtStart()
        return
    if index==self.size-1
        deleteFromEnd()
        return
curr = self.headfor i in range(index-1)
   curr = curr.next
temp = curr.next
curr.next = temp.next
temp.next = None
return temp


                   
