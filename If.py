# Conditional Statement
num = int(input("Integer Number: "))

if num > 0 :
    print("Positive Number")
if num < 0 :
    print("Negative Number")
if num == 0 :
    pirnt("Zero")

# Datetime Module
import datetime
now = datetime.datetime.now()

print("{}Y {}M {}D {}H {}M {}S".format(
    now.year, now.month, now.day, 
    now.hour, now.minute, now.second
))

# IF Hour
if now.hour < 12:
    print("It's {} A.M.".format(now.hour))
if now.hour >= 12:
    print("It's {} P.M.".format(now.hour))

# IF Season
if 3 <= now.month <= 5:
    print("It's Spring in {}.".format(now.month))
if 6 <= now.month <= 8:
    print("It's Summer in {}.".format(now.month))
if 9 <= now.month <= 11:
    print("It's Autumn in {}.".format(now.month))
if now.month == 12 or 1 <= now.month <= 2:
    print("It's Winter in {}.".format(now.month))