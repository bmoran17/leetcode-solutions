# 1920. Build Array from Permutation - https://leetcode.com/problems/build-array-from-permutation/description/
# Given a zero-based permutation nums (0-indexed), build an array ans of the same length where ans[i] = nums[nums[i]] for each 0 <= i < nums.length and return it.
# A zero-based permutation nums is an array of distinct integers from 0 to nums.length - 1 (inclusive).

def buildArray(nums: list[int]) -> list[int]:
  return [nums[i] for i in nums]

print(buildArray([0, 2, 1, 5, 3, 4])) # [0, 1, 2, 4, 5, 3]
print(buildArray([5, 0, 1, 2, 3, 4])) # [4, 5, 0, 1, 2, 3]

