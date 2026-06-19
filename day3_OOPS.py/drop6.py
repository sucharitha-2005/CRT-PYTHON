# Parent class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(self.name)


# Child class
class Dog(Animal):
    pass


# Create object
d1 = Dog("Rex")

# Call method
d1.speak()
