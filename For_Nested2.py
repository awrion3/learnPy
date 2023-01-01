output = ""

for i in range(1, 15):
    for j in range(14, i, -1): #if i=1 : 14~2 [13]
        output += " "
    for k in range(0, 2*i-1):
        output += "*"
    output += "\n"

print(output)