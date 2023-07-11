#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# my code is here
j = abs(number) % 10
# j for last digits
if number < 10:
    j *= -1
if j > 5 and j != 0:
    print('Last digit of {} is {} and is greater than 5'.format(number,
                                                                j))
elif j < 6 and j != 0:
    print('Last digit of {} is {} and is less than 6 and not 0'
          .format(number, j))
else:
    print('Last digit of {} is {} and is 0'.format(number, j))
