class student:
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
    
    def to_string(self):
        return "{}\t{}\t{}".format(\
            self.name,\
            self.get_sum(),\
            self.get_ave())

students = [
    student("A", 87, 98, 88, 95),
    student("B", 92, 98, 96, 98),
    student("C", 76, 96, 94, 90),
    student("D", 98, 92, 96, 92),
    student("E", 95, 98, 98, 98),
    student("F", 64, 88, 92, 92)
]

print("name", "sum", "ave", sep="\t")
for student in students:
    print(student.to_string())