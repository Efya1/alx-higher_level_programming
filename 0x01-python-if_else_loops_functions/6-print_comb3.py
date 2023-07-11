#!/usr/bin/python3
x = 0
while x < 8:
    y = x
    while y <= 9:
        if x != y:
            print('{}{}'.format(x, y), end=', ')
        y += 1
    x += 1
print('{}{}'.format(x, y - 1), sep='')
