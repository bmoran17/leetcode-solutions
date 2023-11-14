# 1725. Number Of Rectangles That Can Form The Largest Square - https://leetcode.com/problems/number-of-rectangles-that-can-form-the-largest-square/description/

def countGoodRectangles(rectangles: list[list[int]]) -> int:
  sqr_len = []
  for i in rectangles:
      sqr_len.append(min(i))
  return sqr_len.count(max(sqr_len))

print(countGoodRectangles([[5,8],[3,9],[5,12],[16,5]])) # 3
print(countGoodRectangles([[2,3],[3,7],[4,3],[3,7]])) # 3
