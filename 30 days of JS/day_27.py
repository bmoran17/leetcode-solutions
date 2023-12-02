from collections import defaultdict
# 2176. Count Equal and Divisible Pairs in an Array - https://leetcode.com/problems/count-equal-and-divisible-pairs-in-an-array/description/
# Given a 0-indexed integer array nums of length n and an integer k, 
# return the number of pairs (i, j) where 0 <= i < j < n, such that nums[i] == nums[j] and (i * j) is divisible by k.

def countPairs(nums: list[int], k: int) -> int:
  # make dictionary 
  d = defaultdict(list)
  # initialize pair count
  pairs = 0

  # enumerate through each number and its index
  for i, n in enumerate(nums):
    # if number is a key in dictionary
    if n in d:
      # iterate through indexes associatde with number 
      for index in d[n]:
        # if index is divisible by k - increment pair count
        if index * i % k == 0:
          pairs += 1
    # append index to key of current number
    d[n].append(i)
  # return pairs count
  return pairs

print(countPairs([3,1,2,2,2,1,3],2)) # 4
print(countPairs([1,2,3,4],1)) # 0