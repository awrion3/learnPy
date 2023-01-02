#
num = int(input("number: "))

if num % 2 == 0:
    print(("Input is {}.\n"
    "{} is even number.")
    .format(num, num)) # prefered form
else :
    print("\n".join([  # .join() + [list] + .format()
        "Input is {}.",
        "{} is odd number."
        ]).format(num, num))

# else :
#    print("""Input is {}.
#    {} is odd number.""".format(num, num)) # indent problem

# str .join()
print("~".join(["A", "B", "1", "2"]))
