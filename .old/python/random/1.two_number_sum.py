'''given a list of integers and a number n, 
   find a pair that sums to the number n'''


#Using hash table - O(n) time and O(n) space
def get_pair_using_hashmap(lst, num):
    num_dict = {}
    for each in lst:
        if (num -each) in num_dict:
            return [each,num-each]
        else:
            num_dict[each]=None
    return []

# using sorted list. O(nlogn) time and O(1) space
def get_pair_using_sorted_list(lst,num):
    lst.sort()
    left = 0
    right=len(lst)-1

    while left < right:
        curr_sum = lst[left] + lst[right]
        if curr_sum < num:
            left+=1
        elif curr_sum > num:
            right-=1
        else:
            return [lst[left],lst[right]]
    return []

if __name__ == "__main__":
    lst = [3,5,-4,8,11,1,-1,6]
    print(get_pair_using_sorted_list(lst,10))
