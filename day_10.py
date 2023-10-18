# 35. Search Insert Position https://leetcode.com/problems/search-insert-position/
# Given a sorted array of distinct integers and a target value, return the index if the target is found. 
# If not, return the index where it would be if it were inserted in order.
# You must write an algorithm with O(log n) runtime complexity.

class Solution:
  def searchInsert(self, nums: List[int], target: int) -> int:
    l = 0
    r = len(nums) - 1
    # while left pointer hasn't cross right pointer
    while l <= r: 
      mid = (l + r) // 2
      # if middle value equals target - return mid
      if target == nums[mid]:
          return mid
      # target is bigger than middle value - update left pointer
      if target > nums[mid]:
          l = mid + 1
      # target is smaller than middle value - update right pointer
      else:
          r = mid - 1
      # return l pointer if value doesn't exist
      return l
        