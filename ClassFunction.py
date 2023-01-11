class Student:
    count = 0
    students = []

    @classmethod
    def print(cls):
        print("< list of students >")
        print("name\tsum\tave")
        for student in cls.students:
            print(str(student))
        print("_____   _____   _____")


    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science
    
        Student.count += 1
        Student.students.append(self)
    
    def get_sum(self):
        return self.korean + self.math +\
            self.english + self.science
    
    def get_ave(self):
        return self.get_sum()/4
    

    def __str__(self):
        return "{}\t{}\t{}".format(\
            self.name,\
            self.get_sum(),\
            self.get_ave())


students = [
    Student("A", 87, 98, 88, 95),
    Student("B", 92, 98, 96, 98),
    Student("C", 76, 96, 94, 90),
    Student("D", 98, 92, 96, 92),
    Student("E", 95, 98, 98, 98),
    Student("F", 64, 88, 92, 92)
]

Student.print()