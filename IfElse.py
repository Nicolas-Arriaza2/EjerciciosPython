'''Task
Given an integer, , perform the following conditional actions:

If  is odd, print Weird
If  is even and in the inclusive range of 2 to 5, print Not Weird
If  is even and in the inclusive range of 6 to 20, print Weird
If  is even and greater than 20, print Not Weird
Input Format

A single line containing a positive integer, .

Constraints

Output Format

Print Weird if the number is weird. Otherwise, print Not Weird.'''


import math
import os
import random
import re
import sys


if __name__ == '__main__':
    n = int(input().strip())

    result = True

    if n % 2 == 0:
        if n < 5:
            result = False
        if n > 5 and n < 21:
            result = True
        if n > 20:
            result = False
    else:
        result = True
    if result:
        print("Weird")
    else:
        print("Not Weird")
