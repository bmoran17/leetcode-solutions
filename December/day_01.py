# 2778. Sum of Squares of Special Elements - https://leetcode.com/problems/sum-of-squares-of-special-elements/description/

def sumOfSquares(nums: list[int]) -> int:
  # initialize sum of squares
  sum = 0
  # iterate through length of nums
  for x in range(len(nums)):
    # if n % i == 0 (divisible)
    # x + 1 due to 1-indexed array
    if (len(nums) % (x + 1) == 0):
      # add squared num 
      sum += nums[x] ** 2
  # return sum of squares
  return sum

print(sumOfSquares([1,2,3,4])) # 21
print(sumOfSquares([2,7,1,19,18,3])) # 63