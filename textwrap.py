'''You are given a string s and width w.
Your task is to wrap the string into a paragraph of width w.

Function Description

Complete the wrap function in the editor below.

wrap has the following parameters:

string string: a long string
int max_width: the width to wrap to
Returns

string: a single string with newline characters ('\n') where the breaks should be

ABCDEFGHIJKLIMNOQRSTUVWXYZ
4

ABCD
EFGH
IJKL
IMNO
QRST
UVWX
YZ

'''

import textwrap
import math


def wrap(string, max_width):
    num_ciclos = math.ceil(len(string) / max_width)
    result = []

    for i in range(num_ciclos):
        start = i * max_width
        end = start + max_width
        result.append(string[start:end])

    return "\n".join(result)


if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
