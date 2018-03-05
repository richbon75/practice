import hashlib

stub = b'iwrupvqb'

for x in range(0, 1000000000):
    if hashlib.md5(stub + bytes(str(x),'utf-8')).hexdigest()[0:5] == '00000':
        print(x)
        break
