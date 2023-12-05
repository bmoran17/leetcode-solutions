# 2942. Find Words Containing Character - https://leetcode.com/problems/find-words-containing-character/description/
def findWordsContaining(words: list[str], x: str) -> list[int]:
  res = []
  for i in range(len(words)):
    if x in words[i]:
      res.append(i)
  return res
  
print(findWordsContaining(["leet","code"], x = "e")) # [0,1]
print(findWordsContaining(["abc","bcd","aaaa","cbc"], x = "a")) # [0,2]
print(findWordsContaining(["abc","bcd","aaaa","cbc"], x = "z")) # []
