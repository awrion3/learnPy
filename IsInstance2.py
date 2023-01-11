class Student:
    def study(self):
        print("Study")

class Teacher:
    def teach(self):
        print("Teach")

classroom = [Student(), Student(), Teacher(), Student(), Student()]

for person in classroom:
    if isinstance(person, Student):
        person.study()
    elif isinstance(person, Teacher):
        person.teach()