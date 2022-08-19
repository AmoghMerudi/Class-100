class Student:
    def __init__(self, name, school, standard, age):
        self.name = name
        self.school = school
        self.standard = standard
        self.age = age

    def setAge(self):
        print("Enter your age")

student1 = Student("Amogh", "Podar International School", 10, 15)
print(student1.name)
print(student1.setAge())
