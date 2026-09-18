class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        l=0
        r=x
        ans=0
        while l<=r:
            mid =l+(r-l)//2
            if mid*mid ==x:
                return mid
            if mid*mid <x:
                ans=mid
                l=mid+1
            else:
                r=mid-1
        return ans
        