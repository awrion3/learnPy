#
def test():
    print("A position")
    return              # end function
    print("B position")

test()

#
def sumAll(start,end):
    output = 0
    for i in range(start, end+1):
        output += i
    return output

print(sumAll(0,100))

#
def sumA(start=0,end=100,step=1): # default p
    out = 0
    for i in range(start, end+1, step):
        out += i
    return out

print(sumA(0,100,10)) # positional arg
print(sumA(end=100)) # keyword arg