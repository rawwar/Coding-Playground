'''Given two lists. Find two elements, one from 1st list and other from 2nd list, such that the
difference between them is the smallest'''


def get_smallest_diff(lst1,lst2):
    lst1.sort()
    lst2.sort()
    left_i = 0
    right_i = 0
    smallest = float("inf")
    current = float("inf")
    smallest_pair = []
    while(left_i < len(lst1) and right_i < len(lst2)):
        first_num = lst1[left_i]
        second_num = lst2[right_i]
        if first_num < second_num:
            current = second_num - first_num
            left_i+=1
        elif second_num < first_num:
            current = first_num - second_num
            right_i +=1
        else:
            return [first_num,second_num]
        if smallest > current:
            smallest = current
            smallest_pair = [first_num,second_num]
    return smallest_pair

if __name__ == "__main__":
    lst1 = [1,2,3,4,5,7,8,34]
    lst2 = [43,21,342,10,43556,47,211]
    print(get_smallest_diff(lst1,lst2))