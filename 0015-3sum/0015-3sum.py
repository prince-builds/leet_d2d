class Solution:

  def threeSum(self, nums: list[int]) -> list[list[int]]:
    res = []
    nums.sort()

    for i in range(len(nums) - 2):
      # Skip duplicate elements for the first position
      if i > 0 and nums[i] == nums[i - 1]:
        continue

      # Early exit if the smallest number is positive
      if nums[i] > 0:
        break

      left, right = i + 1, len(nums) - 1
      while left < right:
        current_sum = nums[i] + nums[left] + nums[right]

        if current_sum == 0:
          res.append([nums[i], nums[left], nums[right]])

          # Skip duplicates for the left pointer
          while left < right and nums[left] == nums[left + 1]:
            left += 1
          # Skip duplicates for the right pointer
          while left < right and nums[right] == nums[right - 1]:
            right -= 1

          left += 1
          right -= 1
        elif current_sum < 0:
          left += 1
        else:
          right -= 1

    return res