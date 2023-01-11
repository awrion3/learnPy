class Parent:
    def __init__(self):
        self.value = "Test"
        print("Parent Class __init()__ method called")
    def test(self):
        print("Parent Class test() method")

class Child(Parent):
    def __init__(self):
        Parent.__init__(self)
        print("Child Class __init()__ method called")

child = Child()
child.test()
print(child.value)