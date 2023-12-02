# 1534. Count Good Triplets - https://leetcode.com/problems/count-good-triplets/description/
def countGoodTriplets(arr: list[int], a: int, b: int, c: int) -> int:
  triplets = 0
  for i in range(len(arr)):
    for j in range(i+1, len(arr)):
      for k in range(j+1, len(arr)):
        if (abs(arr[i] - arr[j]) <= a) and (abs(arr[j] - arr[k]) <= b) and (abs(arr[i] - arr[k]) <= c):
            triplets += 1
  return triplets

print(countGoodTriplets([3,0,1,1,9,7],7,2,3)) # 4
print(countGoodTriplets([1,1,2,2,3],0,0,1)) # 0