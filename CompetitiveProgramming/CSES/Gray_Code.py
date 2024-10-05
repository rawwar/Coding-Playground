n = int(input())

def gray_codes(n):
    if n == 1:
        return ["0", "1"]
    else:
        lst = gray_codes(n-1)
        lst2 = []
        for each in lst:
            lst2.append("0"+each)
        for each in lst[::-1]:
            lst2.append("1"+each)
        return lst2

for each in gray_codes(n):
    print(each)

    Demat account number: IN303028
    client id: 95708934