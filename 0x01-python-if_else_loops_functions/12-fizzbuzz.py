#!/usr/bin/python3
def fizzbuzz():
    str1 = 'Fizz'
    str2 = 'Buzz'
    for y in range(1, 101):
        if y % 3 == 0 and y % 5 == 0:
            print('{:s}'.format(str1 + str2), end=' ')
        elif y % 3 == 0 and y % 5 != 0:
            print('{:s}'.format(str1), end=' ')
        elif y % 3 != 0 and y % 5 == 0:
            print('{:s}'.format(str2), end=' ')
        else:
            print('{}'.format(y), end=' ')
        if y == 100:
            print(end='')
