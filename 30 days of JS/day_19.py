# 1528. Shuffle String - https://leetcode.com/problems/shuffle-string/description/
# You are given a string s and an integer array indices of the same length. 
# The string s will be shuffled such that the character at the ith position moves to indices[i] in the shuffled string.
# Return the shuffled string.

def restoreString(s: str, indices: list[int]) -> str:
  # array for shuffling - length of string
  res = [''] * len(s)
  # iterate length of string
  for i in range(len(s)):
    # set character at corresponding index
    res[indices[i]] = s[i]
    # joins all elements into string
  return ''.join(res)

print(restoreString("codeleet", [4,5,6,7,0,2,1,3])) # "leetcode"
print(restoreString("abc", [0,1,2])) # "abc"
