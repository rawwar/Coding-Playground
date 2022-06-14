t = int(input())

for _ in range(t):
    input()
    start = False
    done = False
    for i in range(1,9):
        inp = input().strip()
        if done:
            continue
        else:
            c = inp.count("#")
            if c == 1:
                if start:
                    print(f"{i} {inp.index('#')+1}")
                    done = True

            elif c == 2:
                start = True
