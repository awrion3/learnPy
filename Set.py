schools = ["A", "B", "C", "A", "C", "C", "D"]

set = set()  # set = set(schools)

for school in schools: # set.update(schools)
    set.add(school)    #

print(f"{len(set)} number of schools, {set}")


# set comprehension
a = {
    item * item
    for item in range(0, 10)
        if item % 2 == 0
}

print(type(a))

# generator expression
a = (
    item * item
    for item in range(0, 10)
        if item % 2 == 0
)

print(type(a))