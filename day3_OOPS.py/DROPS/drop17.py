class Animal:
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        print("Bow Bow")

class Cat(Animal):
    def sound(self):
        print("Meow")

class Cow(Animal):
    def sound(self):
        print("Moo")


# Creating objects
dog = Dog()
cat = Cat()
cow = Cow()

# Output
dog.sound()
cat.sound()
cow.sound()