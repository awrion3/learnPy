class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

class StudentList:
    def __init__(self):
        self.students = []
    
    def append(self, student):
        self.students.append(student)

    def get_average(self):
        return sum([
            student.score for student in self.students
        ]) / len(self.students)
    
    def get_first_by_score(self):
        return max(self.students, key= lambda x: x.score)
    
    def get_last_by_score(self):
        return min(self.students, key= lambda x: x.score)

students = StudentList()
students.append(Student("Cloud", 100))
students.append(Student("Star", 49))
students.append(Student("Choco", 81))
students.append(Student("Moon", 90))

print(f"average is {students.get_average()}")
print(f"first student is {students.get_first_by_score().name}")
print(f"last student is {students.get_last_by_score().name}")