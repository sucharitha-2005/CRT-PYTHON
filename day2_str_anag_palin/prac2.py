class Student:
    branch ="it"
    college ="mlwec"
    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno
        

    def playing(self):
        return f"{self.name} is playing"

    def eating(self):
        return f"{self.name} is eating"

    def sleeping(self):
        return f"{self.name} is sleeping"


s1 = Student("Rahul", 101)
S2 = Student("suha", 102)
s3 = Student("maha", 103)
print(s1.playing())
