
def has_vowels(x):
    z = [y for y in filter(lambda m: m in ('a','e','i','o','u'), list(x))]
    if len(z) >= 3:
        return True
    return False

def has_double(x):
    last_letter = None
    for letter in x:
        if letter == last_letter:
            return True
        last_letter = letter
    return False

def not_forbidden(x):
    if 'ab' in x or 'cd' in x or 'pq' in x or 'xy' in x:
        return False
    return True

def is_nice(x):
    return has_vowels(x) and has_double(x) and not_forbidden(x)

nice = 0
f = open('a05_input.txt')
for line in f:
    if is_nice(line.strip()):
        nice += 1
f.close()
print('nice = ', nice)
