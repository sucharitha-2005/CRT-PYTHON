class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
Node1 = Node(10)
Node2 = Node(20)
Node1.data = 30
Node1.next = Node2
print(Node1.next.data)
print(Node2.data)