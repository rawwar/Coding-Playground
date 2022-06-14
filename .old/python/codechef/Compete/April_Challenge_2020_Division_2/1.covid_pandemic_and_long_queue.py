'''https://www.codechef.com/APRIL20B/problems/COVIDLQ'''

T =int(input())

for i in range(T):
    n = input()
    lst = list(map(int,input().split()))
    result = True
    start = False
    counter = 0
    for each in lst:
        if each == 1:
            if start:
                if counter < 5:
                    result = False
                    break

            else:
                start = True
            counter = 0
        else:
            if start:
                counter += 1
    
    if result:
        print("YES")
    else:
        print("NO")

        