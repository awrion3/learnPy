#
def flatten(data):
    output = []
    
    for i in data:
        if type(i) == list:
            output += flatten(i) # += : .extend()
        else: 
            output.append(i)

    return output

ex = [[1, 2, 3], [4, [5, 6]], 7, [8, 9]]
print(ex)
print(flatten(ex))

#
def p(content):
    return "<p class='content-line'>{}</p>".format(content)

print(p("Hello."))