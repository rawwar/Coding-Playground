T = int(input())

hm = {"A":"T","T":"A","C":"G","G":"C"}

for _ in range(T):
    n = int(input())
    s = input()
    print("".join([hm[i] for i in s]))

