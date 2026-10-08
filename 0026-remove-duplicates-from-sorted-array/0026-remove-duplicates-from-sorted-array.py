class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:

        n=len(nums)
       
        start=0
        for i in range(n):
            if nums[i]!= nums[start]:
                start+=1

                # nums[i]=nums[start]
                nums[start]=nums[i]
        return start+1
        