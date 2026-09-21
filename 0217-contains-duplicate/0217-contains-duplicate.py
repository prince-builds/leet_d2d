class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        seen=set()
        for s in nums:
            if s  in seen:
                return True
            seen.add(s)
        return False
        