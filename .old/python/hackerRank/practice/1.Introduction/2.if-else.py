#!/bin/python3

N = int(input())

if N%2 != 0:
    print("Weird")
else:
    if N in [2,3,4,5]:
        print("Not Weird")
    elif N in list(range(6,21)):
        print("Weird")
    else:
        print("Not Weird")
