#
def fact(n):
    out = 1
    for i in range(1, n+1):
        out *= i
    return out

print(fact(4))

# recursion
def factor(n):
    if n == 0:
        return 1
    else :
        return n*factor(n-1)

print(factor(4))

# recursion 2
counter = 0

def fibo(n):
    
    global counter # global: refer to variable 'counter' from outside of function
    counter += 1
    print("count: %d" %counter)

    if n == 1:
        return 1
    if n == 2 :
        return 1
    else:
        return fibo(n-1) + fibo(n-2)

print(fibo(4))

# memoization
dic = {
    1: 1,
    2: 1
}

def fib(n):
    if n in dic:
        return dic[n]
    else:
        output = fib(n-1) + fib(n-2)
        dic[n] = output
        return output

print(fib(4))

# early return
def fibs(n):
    if n in dic:
        return dic[n]

    output = fibs(n-1) + fibs(n-2)
    dic[n] = output
    return output

print(fibs(4))