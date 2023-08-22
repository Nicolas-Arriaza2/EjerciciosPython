'''
The included code stub will read an integer, n, from STDIN.

Without using any string methods, try to print the following:
123....n

Note that "..." represents the consecutive values in between.

Example
n=5
Print the string 12345.

Input Format

The first line contains an integer n.


'''


if __name__ == '__main__':
    n = int(input())
    j = ''
    i = 1
    while i <= n:
        j += str(i)
        i += 1

    print(j)
