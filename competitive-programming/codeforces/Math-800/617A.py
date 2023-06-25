n = int(input())
 
if n <=5 :
    print(1)
else:
    res = 0
    res += n//5
    if n%5 != 0:
        res += 1
    print(res)