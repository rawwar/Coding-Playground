class Solution:
    def getRow(self, rowIndex):
        curr = [1]
        if rowIndex == 0:
            return curr
        for i in range(rowIndex+1):
            curr = [1] + [curr[j] + curr[j+1] for j in range(i-1)] + [1]
        return curr

if __name__ == "__main__":
    obj = Solution()
    print(obj.getRow(3))