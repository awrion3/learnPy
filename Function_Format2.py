# integer type
F1 = "{:+5d}".format(52)  # \\+52
F2 = "{:+5d}".format(-52) # \\-52
print(F1)
print(F2)

F3 = "{:=+5d}".format(52)  # +\\52
F4 = "{:=+5d}".format(-52) # -\\52
print(F3)
print(F4)

F5 = "{:+05d}".format(52)  # +0052
F6 = "{:+05d}".format(-52) # -0052
print(F5)
print(F6)


# float type "{:f}".format()
f0 = "{:+011f}".format(52.234) # +052.234000 (.ffffff 7)
print(f0)

# other float type formats
f1 = "{:6.3f}".format(52.273) # 52.273
f2 = "{:6.2f}".format(52.273) # /52.27
f3 = "{:6.1f}".format(52.273) # //52.3 (auto round)
print(f1)
print(f2)
print(f3)

# remove .0
f4 = "{:g}".format(25.0)
print(f4)