# Given list of start, end times. check if its possible to attend all

def solution(lst):
    sorted_lst = sorted(lst, key=lambda x: x[0])
    for i in range(len(lst)-1):
        if lst[i][1] > lst[i+1][0]:
            return False
    return True


if __name__ == "__main__":
    lst = [[0,30],[5,10],[15,20]]
    assert solution(lst) == False