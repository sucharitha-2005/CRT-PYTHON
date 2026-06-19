class Student:
    branch = "it"
    college = "mlwec"

    def __init__(self, name, rollno):
        self.__name = name      # private attribute
        self.__rollno = rollno  # private attribute

    def get_name(self):
        return self.__name

    def get_rollno(self):
        return self.__rollno

    def playing(self):
        return f"{self.__name} is playing"

    def eating(self):
        return f"{self.__name} is eating"

    def sleeping(self):
        return f"{self.__name} is sleeping"


s1 = Student("Rahul", 101)

print(s1.playing())
print(s1.get_name())
print(s1.get_rollno())

# This will raise an error:
# print(s1.__name)