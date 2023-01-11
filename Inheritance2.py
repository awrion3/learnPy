class CustomException(Exception):
    def __init__(self, message, value):
        Exception.__init__(self)
        self.message = message
        self.value = value

    def __str__(self):
        return self.message
    
    def print(self):
        print(self.message)
        print(self.value)
    
try:
    raise CustomException("Error Created", 576)
except CustomException as e:
    e.print()