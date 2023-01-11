class Test:
    def __init__(self, name):
        self.name = name
        print("{} generated".format(self.name))
    def __del__(self):
        print("{} destroyed".format(self.name))

a = Test("A")
b = Test("B")
c = Test("C")