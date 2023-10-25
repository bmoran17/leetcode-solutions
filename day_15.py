# 1512. Number of Good Pairs - https://leetcode.com/problems/number-of-good-pairs/description/
# Given an array of integers nums, return the number of good pairs.
# A pair (i, j) is called good if nums[i] == nums[j] and i < j.

def numIdenticalPairs(nums: list[int]) -> int:
  pairs = 0
  for i in range(len(nums)):
    # compare to values after i 
    for j in range(i + 1, len(nums)):
      # if values match - add pair to counter
      if nums[i] == nums[j]:
        pairs += 1 

  return pairs

print(numIdenticalPairs([1,2,3,1,1,3])) # 4
print(numIdenticalPairs([1,1,1,1])) # 6
print(numIdenticalPairs([1,2,3])) # 0