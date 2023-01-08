def test(function):
    def wrapper():
        print("Start")
        function()
        print("End")
    return wrapper

@test
def hello():
    print("hello")

hello()

#
from functools import wraps

def test(function):
    @wraps
    def wrapper(*arg, **kwargs):
        print("Start")
        function()
        print("End")
    return wrapper
