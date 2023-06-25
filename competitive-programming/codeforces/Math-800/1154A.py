lst = list(map(int, input().split()))

highest = max(lst)


res = [str(highest-i) for i in lst if highest-i >0]

print(" ".join(res))