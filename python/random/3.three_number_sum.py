''' Given a list of unique integers and a number n, find triplet that sum to the number n'''

# Using sorting - O(N^2) time and O(N) space

def get_triplet_by_sorting(lst, value):
    lst.sort()
    triplets = []
    for i in range(len(lst)-2):
        left = i+1
        right = len(lst)-1
        while left < right:
            curr_sum = lst[i] + lst[left]+ lst[right]
            if curr_sum <value:
                left += 1
            elif curr_sum > value:
                right -= 1
            else:
                triplets.append([lst[i],lst[left],lst[right]])
                left += 1
                right -= 1
    return triplets


if __name__ == "__main__":
    lst = [-4,-2, -6, 0,2,4,8,10]
    print(get_triplet_by_sorting(lst,0))