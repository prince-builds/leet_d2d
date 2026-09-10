class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        dictt={}
        for i in range(n):
            rem=target-nums[i]
            if rem in dictt:
                return [dictt[rem],i]
            dictt[nums[i]]=i
        