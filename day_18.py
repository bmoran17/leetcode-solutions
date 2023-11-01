# 1389. Create Target Array in the Given Order - https://leetcode.com/problems/create-target-array-in-the-given-order/

def createTargetArray(nums: list[int], index: list[int]) -> list[int]:
  target = []
  for n, i in zip(nums,index): 
    target.insert(i,n)
  return target

print(createTargetArray([0,1,2,3,4], [0,1,2,2,1])) # [0,4,1,3,2]
print(createTargetArray([1,2,3,4,0], [0,1,2,3,0])) # [[0,1,2,3,4]
print(createTargetArray([1], [0])) # [1]