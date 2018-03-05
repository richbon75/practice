
# probably doesn't make sense in Python

def urlify(value):
    output = ''
    for char in value:
        if char == ' ':
            output += '%20'
        else:
            output += char
    return output

def urlify_replace(value):
    return value.replace(' ','%20')
