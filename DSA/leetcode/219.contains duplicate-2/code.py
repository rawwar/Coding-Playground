class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hm = {}
        for idx, each in enumerate(nums):
            if each in hm and (idx - hm[each] <= k):
                return True
            hm[each] = idx
        return False