class Solution:
    def searchInsert(self, nums,target):
        n=len(nums)
        left=0
        right=n-1
        ans=0
        while left<=right:
            mid=left+(right-left)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]<target:
                left=mid+1
            else:
                right=mid-1
        return left
        