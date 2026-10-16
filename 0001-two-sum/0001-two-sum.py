class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        dict1={}

        for i in range(len(nums)):
            rem= target-nums[i]
            if rem in dict1:
                return [dict1[rem],i]
            dict1[nums[i]]=i
        