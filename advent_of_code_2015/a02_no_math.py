total_order = 0
ribbon = 0
f = open('a02_input.txt', 'r')
for line in f:
    l, w, h = (int(x) for x in line.strip().split('x'))
    s1 = l * w
    s2 = w * h
    s3 = l * h
    total_order += 2*(s1 + s2 + s3) + min(s1, min(s2, s3))
    ribbon += (2*(min(l+w, min(w+h, h+l)))) + (l*w*h)
f.close()
print('total order = ', total_order)
print('total ribbon = ', ribbon)



    
