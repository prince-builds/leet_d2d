class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        n=len(nums)
        l=0
        total=sum(nums)
        for i in range(n):
            r=total-l-nums[i]


            if l==r:
                return i
            l+=nums[i]
        return -1
        
        