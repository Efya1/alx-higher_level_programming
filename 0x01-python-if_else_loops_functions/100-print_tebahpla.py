#!/usr/bin/python3
for y in range(ord('z'), ord('a') - 1, -1):
    if y % 2 == 0:
        x = 0
    else:
        x = 1
    print('{:s}'.format(chr(y - (x * 32))), end='')
