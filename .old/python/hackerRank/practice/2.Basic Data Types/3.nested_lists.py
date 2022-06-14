students = []
scores_lst=[]
for _ in range(int(input())):
    name = input()
    score = float(input())
    scores_lst.append(score)
    students.append([name,score])
scores_unique = list(set(scores_lst))
y = sorted(scores_unique)[1]
temp = [i[0] for i in students if i[1]==y]
temp.sort()
print("\n".join(temp))
