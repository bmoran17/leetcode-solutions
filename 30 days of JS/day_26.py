# 1732. Find the Highest Altitude - https://leetcode.com/problems/find-the-highest-altitude/description/
def largestAltitude(gain: list[int]) -> int:
  altitudes = [0]
  for i in gain:
    altitudes.append(i + altitudes[-1])
  return max(altitudes)

print(largestAltitude([-5,1,5,0,-7])) # 1
print(largestAltitude([-4,-3,-2,-1,4,3,2])) # 0