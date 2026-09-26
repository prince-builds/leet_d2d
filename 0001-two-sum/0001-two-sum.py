class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        d={}

        for i in range(len(nums)):
            rem=target -nums[i]
            if rem in d:
                return [d[rem],i]
            d[nums[i]]=i
        