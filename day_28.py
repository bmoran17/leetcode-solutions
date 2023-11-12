# 1295. Find Numbers with Even Number of Digits - https://leetcode.com/problems/find-numbers-with-even-number-of-digits/description/
# Given an array nums of integers, return how many of them contain an even number of digits.

def findNumbers(nums: list[int]) -> int: 
  res = 0
  for num in nums:
    if len(str(num)) % 2 == 0:
      res += 1
  return res

print(findNumbers([12,345,2,6,7896])) # 2
print(findNumbers([555,901,482,1771])) # 1