s = input()

max_count = 1

curr_max = 1

l = 1

while l < len(s):
    if s[l] == s[l-1]:
        curr_max += 1
    else:
        curr_max=1
    l+=1
    max_count = max(max_count, curr_max)

print(max_count)