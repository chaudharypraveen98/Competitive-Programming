#!/bin/python3
import os


def rotLeft(a, d):
    remainder = len(a)//d
    print(remainder)
    if(len(a) >= d):
        return a[d:]+a[0:d]
    return a[remainder:]+a[0:remainder]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    a = list(map(int, input().rstrip().split()))

    result = rotLeft(a, d)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
