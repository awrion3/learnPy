class Student:
    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science

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

#
    def __eq__(self, value):
        return self.get_sum() == value.get_sum()
    
    def __ne__(self, value):
        return self.get_sum() != value.get_sum()

    def __gt__(self, value):
        return self.get_sum() > value.get_sum()
    
    def __ge__(self, value):
        return self.get_sum() >= value.get_sum()

    def __lt__(self, value):
        return self.get_sum() < value.get_sum()

    def __le__(self, value):
        return self.get_sum() <= value.get_sum()

students = [
    Student("A", 87, 98, 88, 95),
    Student("B", 92, 98, 96, 98),
    Student("C", 76, 96, 94, 90),
    Student("D", 98, 92, 96, 92),
    Student("E", 95, 98, 98, 98),
    Student("F", 64, 88, 92, 92)
]

print("name", "sum", "ave", sep="\t")
for student in students:
    print(str(student))

#
stuA = Student("A", 87, 98, 88, 95)
stuB = Student("B", 92, 98, 96, 98)

print()
print("stuA == stuB", stuA == stuB)
print("stuA != stuB", stuA != stuB)
print("stuA > stuB", stuA > stuB)
print("stuA >= stuB", stuA >= stuB)
print("stuA < stuB", stuA < stuB)
print("stuA <= stuB", stuA <= stuB)

#def __eq__(self, value):
#    if not isinstance(value, Student):
#        raise TypeError("Only Compare Student Class instance")
#    return self.get_sum() == value.get_sum()