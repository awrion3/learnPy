#
file = open("basic.txt", "w")

file.write("Hello Python!")

file.close()

# open & close = with

# write()
with open("basic.txt", "w") as file:
    file.write("Hello Python Programming!")

# read()
with open("basic.txt", "r") as file:
    contents = file.read()
print(contents)