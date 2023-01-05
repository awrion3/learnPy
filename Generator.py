# yield 
def test():
    print("A")
    yield 1
    print("B")
    yield 2
    print("C")

    #StopIteration Error

out = test()

# next()
a = next(out) # return value : 1
print(a)

b = next(out)
print(b)

c = next(out)
print(c)
