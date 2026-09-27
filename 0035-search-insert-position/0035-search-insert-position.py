class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        n=len(nums)
        l=0
        r=n-1
    
        while l<=r:
            m=l+(r-l)//2

            if nums[m]==target:
                return m
            if nums[m]<target:
                l=m+1
            else:
                r=m-1
        return l


        