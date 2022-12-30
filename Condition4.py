sp = input("Say hello or time: ")

import datetime
now = datetime.datetime.now()
hour = now.hour

if "hello" in sp :
    print("Hello")
elif "time" in sp :
    print("It's {}.".format(hour))
else :
    print(sp)