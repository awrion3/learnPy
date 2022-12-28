#  f"{}"  vs  "{}".format() 

print("3 + 4 = " + str(3+4))

print("3 + 4 = {}".format(3+4))

print(f"3 + 4 = {3+4}") # is better

print()
data = ['star', 2, 'M', True]

print(f"""A: {data[0]}
B: {data[1]}
C: {data[2]}
D: {data[3]}""")

print("""A: {}
B: {}
C: {}
D: {}""".format(*data)) # is better
