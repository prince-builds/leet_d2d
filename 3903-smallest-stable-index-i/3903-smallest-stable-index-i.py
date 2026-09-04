class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        
        # suffix_min[i] will store min(nums[i..n-1])
        suffix_min = [0] * n
        suffix_min[-1] = nums[-1]
        for i in range(n - 2, -1, -1):
            suffix_min[i] = min(nums[i], suffix_min[i + 1])
            
        current_max = 0
        for i in range(n):
            current_max = max(current_max, nums[i])
            # instability score = max(nums[0..i]) - min(nums[i..n-1])
            if current_max - suffix_min[i] <= k:
                return i
                
        return -1