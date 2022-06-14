"""https://www.hackerrank.com/contests/hack-the-interview-global/challenges/Heads-or-Tails"""


N = int(input())
tosses = []
for each in range(N):
    tosses.append(input())

def get_maximum_streaks(tosses):
    max_Tails = max_Heads = 0
    Heads = Tails = 0
    iterator = iter(tosses)
    prev = next(iterator)
    if prev == "Heads":
        Heads+=1
    else:
        Tails+=1
    for curr in iterator:
        if curr == prev:
            if curr == "Heads":
                Heads += 1
            else:
                Tails += 1
        elif curr == "Heads":
            if Tails > max_Tails:
                max_Tails = Tails
                Tails = 0
            Heads = 1
                
        elif curr == "Tails":
            if Heads > max_Heads:
                max_Heads = Heads
                Heads = 0
            Tails = 1
        prev = curr
    if Tails > max_Tails:
        max_Tails = Tails
    if Heads > max_Heads:
        max_Heads = Heads
    return(max_Heads,max_Tails)

        
