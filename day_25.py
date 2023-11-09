# 1588. Sum of All Odd Length Subarrays - 1588. Sum of All Odd Length Subarrays
# Given an array of positive integers arr, return the sum of all possible odd-length subarrays of arr.
# A subarray is a contiguous subsequence of the array.

def sumOddLengthSubarrays(arr: list[int]) -> int:
  sum = 0
  # iterate indexes of arr
  for i in range(len(arr)):
    # number of positions that left and right brackets can be placed
    left = i + 1 
    right = len(arr) - i
    # total number of subarrays
    subarrays = left * right
    # if subarrays is even, we divide subarrays by 2
    # when odd we divide by 2 and add 1 (corner case)
    oddarrays = subarrays // 2 if subarrays % 2 == 0 else subarrays // 2 + 1
    # calculate and add to total sum of number in position i that contributes to sum
    sum += oddarrays * arr[i]
  return sum

print(sumOddLengthSubarrays([1,4,2,5,3])) # 58
print(sumOddLengthSubarrays([10,11,12])) # 66
print(sumOddLengthSubarrays([1,2])) # 3