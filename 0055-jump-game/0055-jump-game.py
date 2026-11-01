class Solution:
    def canJump(self, nums: list[int]) -> bool:
        n=len(nums)
        maxx=0

        for i in range(n):
            if i>maxx:
                return False
            maxx=max(maxx,i+nums[i])
        return True

         