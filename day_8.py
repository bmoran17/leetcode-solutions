# 27. Remove Element https://leetcode.com/problems/remove-element/description/
# Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. 
# The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

#Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:
# - Change the array nums such that the first k elements of nums contain the elements which are not equal to val. 
# - The remaining elements of nums are not important as well as the size of nums.
# - Return k.

class Solution:
  def removeElement(self, nums: List[int], val: int) -> int:
    # right pointer for positioning
    i = 0
    # left pointer to compare each element to value
    for j in range(len(nums)):
      # if value doesn't match value in left pointer
      if val != nums[j]:
        # set value in right pointer position
        nums[i] = nums[j]
        # go to next position in array
        i += 1
    # i is number of different values
    return i