"""https://www.hackerrank.com/contests/hack-the-interview-global/challenges/charity"""



import os
import sys

#
# Complete the guestTable function below.
#
def guestTable(generosities):
    #
    # Write your code here.
    #
    ...


#
# Complete the solve function below.
#
def solve():
    #
    # Write your code here.
    #
    ...

if __name__ == '__main__':
    tc = input()
    for tc_itr in range(tc):
        mn = input().split()

        m = int(mn[0])

        n = int(mn[1])

        charm = []

        for _ in range(m):
            charm.append(list(map(int, input().rstrip().split())))

        t = int(input())

        for t_itr in range(t):
            x = int(input())

            generosities = list(map(int, input().rstrip().split()))

            guestTable(generosities)

        k = int(input())

        solve()

'''
Sample input

4
3 3 3
1 2 3
4 5 6
7 8 9
3 10 20 30
3 40 50 60
3 70 80 90
3
3 3 3
1 2 3
4 5 6
7 8 9
2 100 200
1 500
2 30 30
1
3 3 3
1 2 3
4 5 6
7 8 9
1 200
2 500 500
3 30 30 30
1
3 3 3
1 2 3
4 5 6
7 8 9
1 200
2 500 500
4 30 30 30 30
1
'''