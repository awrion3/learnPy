from flask import Flask

from urllib import request
from bs4 import BeautifulSoup

app = Flask(__name__)
@app.route("/")

def hello():
    target = request.urlopen("https://www.weather.go.kr/w/index.do")

    soup = BeautifulSoup(target, "html.parser")

    out = ""
    for loc in soup.select("location"):
        out += "<h3>{}</h3>".format(loc.select_one("city").string)
        out += "Weather: {}<br/>".format(loc.select_one("wf").string)
        out += "Celsius: {}/{}"\
            .format(\
                loc.select_one("tmn").string,\
                loc.select_one("tmx").string\
                    )
        out += "<hr/>"

    return out
