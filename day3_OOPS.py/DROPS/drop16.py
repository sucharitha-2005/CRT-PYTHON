class Teacher:
    def __init__(self, name, age, subject, salary):
        super().__init__(name, age)
        self.subject = subject
        self.salary = salary


teacher = Teacher("Mrs. Sharma", 35, "Math", 50000)

print(teacher.name, teacher.age, teacher.subject, teacher.salary) 