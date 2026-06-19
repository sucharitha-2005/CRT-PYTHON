class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

Node1 = Node(10)
Node2 = Node(20)
Node3 = Node(30)

Node1.next = Node2
Node2.next = Node3

Node1.data = 100
Node2.data = 200
Node3.data = 300


print(Node1.data)           
print(Node1.next.data)      
print(Node1.next.next.data) 