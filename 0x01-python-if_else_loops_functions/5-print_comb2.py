#!/usr/bin/python3
k = 0
while k < 100:
    if k != 99:
        print('{0:02d}'.format(k), end=', ')
    else:
        print(k)
    k += 1
