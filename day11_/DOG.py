class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"{self.name} says: Woof! Woof!")

# Create a dog object
dog1 = Dog("Buddy", "Golden Retriever")

# Make the dog bark
dog1.bark()