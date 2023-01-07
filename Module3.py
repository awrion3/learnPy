#
import time

print("stop for 5 secs")
time.sleep(5)
print("end program")

#
from urllib import request

target = request.urlopen("https://google.com")
output = target.read()

print(output)

#
from operator import itemgetter

books = [{"title":"python", "cost":"18000"
}, {"title":"c", "cost":"24000"
}, {"title":"java", "cost":"23000"}]

print(min(books, key=itemgetter("cost")))
print(max(books, key=itemgetter("cost")))
