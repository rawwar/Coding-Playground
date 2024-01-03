# Given list of start, end times.. calculate min number of rooms required

class Solution:
    def solve(self, lst):
        lst.sort()
        start = 0
        end = 0
        res = 0
        count = 1
        while start < len(lst) and end < len(lst):
            if lst[start][0] == lst[end][1]:
                end += 1
                count -= 1
                continue
            if lst[start] < lst[end]:
                count += 1
                start += 1
            else:
                count -= 1
                end += 1
            res = max(count, res)
        return res 
        
        

if __name__ == "__main__":
    obj = Solution()
    inp1 = [[0, 30],[5, 10],[15, 20]]
    out1 = 2
    inp2 =[[7,10],[2,4]]
    out2 = 1
    assert out1 == obj.solve(inp1)
    assert out2 == obj.solve(inp2)