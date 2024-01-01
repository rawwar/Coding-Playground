class Solution:
    def generate(self, numRows):
        res = [[1], [1, 1]]
        for i in range(2, numRows):
           res2 = [1] +  [res[-1][j]+res[-1][j+1] for j in range(i-1)] + [1]
           res.append(res2)
        return res

if __name__ == "__main__":
    obj = Solution()
    print(obj.generate(10)) 