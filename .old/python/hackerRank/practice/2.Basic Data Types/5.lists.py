N = int(input())
lst = []
for i in range(N):
    val = input().split()
    if val[0]=="print":
        print(lst)
    elif val[0]=="insert":
        lst.insert(int(val[1]),int(val[2]))
    elif val[0]=="remove":
        lst.remove(int(val[1]))
    elif val[0]=="sort":
        lst.sort()
    elif val[0]=="reverse":
        lst.reverse()
    elif val[0]=="pop":
        lst.pop()
    elif val[0]=="append":
        lst.append(int(val[1]))

