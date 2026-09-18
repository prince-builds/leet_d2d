class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        n=len(nums)
        l=0
        r=n-1
        while l<=r:
            mid=l+(r-l)//2

            if nums[mid]==target:
                return mid
            if nums[mid]<target:
                l=mid+1
            else:
                r=mid-1
        return l
        