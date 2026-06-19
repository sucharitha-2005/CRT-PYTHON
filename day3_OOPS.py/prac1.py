class Student:
    def __init__(self, name, rollno, branch, college):
        self.name = name
        self.rollno = rollno
        self.branch = branch
        self.college = college

    def playing(self):
        return f"{self.name} is playing"

    def eating(self):
        return f"{self.name} is eating"

    def sleeping(self):
        return f"{self.name} is sleeping"


s1 = Student("Rahul", 101, "CSE", "ABC College")
print(s1.sleeping())
