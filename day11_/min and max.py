class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.items:
            print("Stack Underflow")
        else:
            print("Popped:", self.items.pop())

    def maxx(self):
        if not self.items:
            print("Stack is empty")
        else:
            print("Maximum element:", max(self.items))

    def display(self):
        print(self.items)


s = Stack()

while True:
    print("\n1.Push  2.Pop  3.Max  4.Display  5.Exit")
    choice = int(input("Enter choice: "))

    if choice == 1:
        item = int(input("Enter element: "))
        s.push(item)

    elif choice == 2:
        s.pop()

    elif choice == 3:
        s.maxx()

    elif choice == 4:
        s.display()

    elif choice == 5:
        break

    else:
        print("Invalid choice")