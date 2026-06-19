class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class singlelinkedlist:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def insertAtstart(self, val):
        newNode = Node(val)

        if self.head is None:
            self.head = self.tail = newNode
        else:
            newNode.next = self.head
            self.head = newNode

        self.size += 1

    def insertAtEnd(self, val):
        newNode = Node(val)

        if self.head is None:
            self.head = self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode

        self.size += 1