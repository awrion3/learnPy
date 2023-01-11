class Student:
    count = 0
    
    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science
    
        Student.count += 1
        print("{} student".format(Student.count))

students = [
    Student("A", 87, 98, 88, 95),
    Student("B", 92, 98, 96, 98),
    Student("C", 76, 96, 94, 90),
    Student("D", 98, 92, 96, 92),
    Student("E", 95, 98, 98, 98),
    Student("F", 64, 88, 92, 92)
]

print("total number of students: {}".format(Student.count))
