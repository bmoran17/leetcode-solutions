# 1662. Check If Two String Arrays are Equivalent
# Given two string arrays word1 and word2, return true if the two arrays represent the same string, and false otherwise.
# A string is represented by an array if the array elements concatenated in order forms the string.

def arrayStringsAreEqual(word1: list[str], word2: list[str]) -> bool:
  first = "".join(word1)
  second = "".join(word2)
  if first == second:
    return True
  return False

print(arrayStringsAreEqual(["ab", "c"], ["a", "bc"])) # True
print(arrayStringsAreEqual(["a", "cb"], ["ab", "c"])) # False
print(arrayStringsAreEqual(["abc", "d", "defg"], ["abcddefg"])) # True