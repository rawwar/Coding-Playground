import sys
n = input()

hm = {}

for each in n:
    if each in hm:
        hm[each] += 1
    else:
        hm[each] = 1

odd_count = 0
odd_char = 0
for each in hm:
    if hm[each] %2 == 0:
        continue
    else:
        odd_count += 1
        odd_char = each
        if odd_count >1:
            print("NO SOLUTION")
            sys.exit(0)
result = odd_char * hm.pop(odd_char) if odd_char != 0 else ""
for each in hm:
    if hm[each] %2 == 0:
        result = (hm[each]//2)*(each) + result + (hm[each]//2)*(each)
print(result)

