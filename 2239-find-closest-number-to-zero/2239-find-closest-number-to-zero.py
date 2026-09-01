class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        close=nums[0]
        for  x in nums:
            if abs(x)<abs(close):
                close = x
                continue
        if  abs(close)==abs(x) and x>close:
            return abs(close)
        else:
            return close
        