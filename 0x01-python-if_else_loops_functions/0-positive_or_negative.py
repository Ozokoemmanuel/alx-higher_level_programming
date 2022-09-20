#!/usr/bin/python3
import random
number = random.randint(-10, 10)
for n in range(number):
    if n > 0:
        print(f"{n} is positive")
        break
    elif n < 0:
        print(f"{n} is negative")
        break
    else:
        print(f"{n} is zero")
