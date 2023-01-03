#
def printN(num, *values): # parameter : *Variable P (variable arguments)
    for i in range(num):
        for v in values:
            print(v)
        print()
printN(3, "How", "are", "you?") # argument

#
def printT(value, n=2): # =Defalut P 
    for i in range(n):
        print(value)

printT("Hi!")

# 
def printS(*values, n=2): # =Keyword P  
    for i in range(n):
        for v in values:
            print(v)
    print()

printS("You're", "doing", "great!", n=4) # =Keyword arg   

#
def test(a, b=10, c=100): # =Default P 
    print(a+b+c)

test(10, 20, 30) # positional arg
test(a=10, b=100, c=200) # keyword arg
test(c=10, a=100, b=200) # keyword arg
test(10, c=200) # positional, keyword arg