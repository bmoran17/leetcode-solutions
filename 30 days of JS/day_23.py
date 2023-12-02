# 2006. Count Number of Pairs With Absolute Difference K - https://leetcode.com/problems/count-number-of-pairs-with-absolute-difference-k/description/?orderBy=most_votes&languageTags=python3

def countKDifference(nums: list[int], k: int) -> int:
  # initialize dictionary and pair count
  seen, pairs = dict(), 0
  # iterate through numbers
  for x in nums:
    # increment pair count by number of times corresponding pair has appeared already
    pairs += seen.get(x-k,0) + seen.get(x+k,0)
    # add 1 to x value in dictionary to keep count of repeats
    seen[x] = seen.get(x,0) + 1
  return pairs

print(countKDifference([1,2,2,1], 1)) # 4
print(countKDifference([3,2,1,5,4], 2)) # 3
print(countKDifference([1,3], 3)) # 0