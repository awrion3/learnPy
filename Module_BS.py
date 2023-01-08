from urllib import request

from bs4 import BeautifulSoup

target = request.urlopen("https://www.weather.go.kr/w/index.do")

soup = BeautifulSoup(target, "html.parser")

for loc in soup.select("location"):
    print(loc.select_one("city").string)    
    print(loc.select_one("wf").string)
    print(loc.select_one("tmn").string)
    print(loc.select_one("tmx").string)
    print()
