class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        st = set()
        for each in nums:
            if each in st:
                return True
            st.add(each)
        return False