# 66. Plus One - https://leetcode.com/problems/plus-one/
# You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. 
# The digits are ordered from most significant to least significant in left-to-right order. 
# The large integer does not contain any leading 0's.
# Increment the large integer by one and return the resulting array of digits.

def plusOne(digits: list[int]) -> list[int]:
  # loop in reverse
  for i in range(len(digits) -1, -1, -1):
    # if digit is 9 - replace with 0 (equals 10, but we carry over the 1)
    if digits[i] == 9:
      digits[i] = 0
    # else just add one to digit
    else:
      digits[i] += 1
      return digits
  # add value 1 to the beginning of the list (happened if all digits were 9)
  return [1] + digits

print(plusOne([1, 2, 3])) # [1, 2, 4]
print(plusOne([9])) # [1, 0]
print(plusOne([4, 3, 2, 1])) # [4, 3, 2, 2]
print(plusOne([9, 9, 9, 9])) # [1, 0 ,0, 0, 0]