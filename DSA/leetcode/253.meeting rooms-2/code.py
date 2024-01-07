# Given list of start, end times.. calculate min number of rooms required

import heapq

class Solution:
    def solve(self, lst):
        lst.sort()
        start = 0
        end = 0
        res = 0
        count = 0
        while start < len(lst) and end < len(lst):
            if lst[start][0] == lst[end][1]:
                end += 1
                count -= 1
                continue
            if lst[start][0] < lst[end][1]:
                count += 1
                start += 1
                end 
            else:
                count -= 1
                end += 1
            res = max(count, res)
        return res
    
    def solve_with_heap(self, lst):
        """
        Main Idea is that, for every new meeting, we need to know if any of the earliest
        are done. if done, we no longer need a new meeting room. we just replace it
        """
        if not lst:
            return 0
        
        lst.sort(key=lambda x:  x[0])
        
        heap = [lst[0][1]]
        for i in range(1, len(lst)):
            if heap and lst[i][0] >= heap[0]:
                heapq.heappop(heap)
            heapq.heappush(heap, lst[i][1])
        
        return len(heap)


if __name__ == "__main__":
    obj = Solution()
    inp1 = [[0, 30],[5, 10],[15, 20]]
    out1 = 2
    inp2 =[[7,10],[2,4]]
    out2 = 1
    print(out1,  obj.solve_with_heap(inp1))
    print(out2, obj.solve(inp2))