#
numbers = [273,103,5,32,65,9,72,800,99]

for item in numbers :
    if len(str(item)) == 1 :
        print("1 digit number") 
    elif len(str(item)) == 2 :
        print("2 digit number")    
    elif len(str(item)) == 3 :
        print("3 digit number")

#
num = [1,2,3,4,5,6,7,8,9]
output = [[],[],[]]

for n in num :
    output[(n+2)%3].append(n)

print(output)

#
N = [1,2,3,4,5,6,7,8,9]

for i in range(0,len(N)//2):
    j = i + (i+1)
    print(f"i={i}, j={j}")
    N[j]= N[j]**2

print(N)
