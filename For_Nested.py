for i in range(9):
    for j in range(9) :
        if j <= i : # i V j >
            print("*", end="")
    else :
        print(" ")

# cf
output = ""
for i in range(1,10):
    for j in range(0,i):
        output += "*"
    output += "\n"
print(output)

# cf2
out = ""

for i in range(1, 10):
    out += ("*"*i)
    out += "\n"
print(out)