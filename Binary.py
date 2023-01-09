from urllib import request

target = request.urlopen("https://www.python.org/static/community_logos/python-logo-master-v3-TM.png")
output = target.read()

print(output)

#
file = open("output.png", "wb")
file.write(output)
file.close