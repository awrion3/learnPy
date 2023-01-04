# callback function

def call(func): # < prin()
    for i in range(10):
        func() 

def prin():
    print("Hello!")

print(call(prin)) # a function that is passed as an argument to other function


# map() # filter()
def power(item):
    return item*item

def under(item):
    return item<3

li = [1, 2, 3, 4, 5]

out1 = map(power, li) # create new list
print(list(out1))

out2 = filter(under, li) # create new list with True value 
print(list(out2))


# lambda parameter: return value
pow = lambda x: x*x
und = lambda x: x<3

l = [1, 2, 3, 4, 5]

outA = map(pow, l)
print(list(outA))

outB = filter(und, l)
print(list(outB))

#
L = [1, 2, 3, 4, 5]
O1 = map(lambda x: x*x, L)
O2 = filter(lambda x: x<3, L)

print(list(O1))
print(list(O2))
