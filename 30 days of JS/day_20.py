# 2535. Difference Between Element Sum and Digit Sum of an Array - https://leetcode.com/problems/difference-between-element-sum-and-digit-sum-of-an-array/description/

def differenceOfSum(nums: list[int]) -> int:
  # initialize digit sum
  digitSum = 0
  # iterate through numbers
  for num in nums:
    # iterate until number becomes 0 (will add last digit one at a time)
    while num != 0:
      # obtain last digit of number - add it to sum
      digitSum += num % 10
      # update number to remove last digit
      num = num // 10
  # return absolute difference of sums
  return abs(sum(nums)-digitSum)

print(differenceOfSum([1,15,6,3])) # 9
print(differenceOfSum([1,2,3,4])) # 0