def swap_case(s):
    temp=""
    for each in s:
        if each.lower() == each:
            temp+=each.upper()
        else:
            temp+=each.lower()
    return temp
if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)