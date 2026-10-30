class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        n=len(nums)
        seen=set()
        l=0
        for r in nums:
            if r in seen:
                return True
            seen.add(r)
        return False
        