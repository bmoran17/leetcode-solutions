# 2824. Count Pairs Whose Sum is Less than Target - https://leetcode.com/problems/count-pairs-whose-sum-is-less-than-target/description/
# Given a 0-indexed integer array nums of length n and an integer target, return the number of pairs (i, j) where 0 <= i < j < n and nums[i] + nums[j] < target.

def countPairs(nums: list[int], target: int) -> int:
  # sort the nums list
  nums.sort() 
  # initialize pairs counter
  pairs = 0 
  # initialize left and right pointers
  l = 0 
  r = len(nums)-1 

  # iterate until left pointer is less than right
  while(l < r): 
    # if sum of pointer elements is less than target
    if(nums[l] + nums[r] < target): 
      # update pairs
      pairs += r - l
      # increment left pointer
      l += 1 
    else:
      # decrement right pointer
      r -= 1 
  return pairs

print(countPairs([-1,1,2,3,1], 2)) # 3
print(countPairs([-6,2,5,-2,-7,-1,3], -2)) # 10