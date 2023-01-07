#
import datetime

print("now")

now = datetime.datetime.now()
print(now.year)
print(now.month)
print(now.day)

print(now.hour)
print(now.minute)
print(now.second)

outA = now.strftime("%Y.%m.%d %H:%M:%S")
outB = "{}Y {}M {}D {}Y {}M {}S".format(now.year,\
    now.month,\
    now.day,\
    now.hour,\
    now.minute,\
    now.second)
outC = now.strftime("%Y{} %m{} %d{} %H{} %M{} %S{}").format(*"YMDHMS")

print(outA)
print(outB)
print(outC)

#
after = now + datetime.timedelta(\
    weeks=1,\
    days=1,\
    hours=1,\
    minutes=1,\
    seconds=1)
print(after.strftime("%Y{} %m{} %d{} %H{} %M{} %S{}").format(*"YMDHMS"))

output = now.replace(year=(now.year + 1))
print(output.strftime("%Y{} %m{} %d{} %H{} %M{} %S{}").format(*"YMDHMS"))
