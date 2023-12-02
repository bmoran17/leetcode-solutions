# 1816. Truncate Sentence - https://leetcode.com/problems/truncate-sentence/description/
# You are given a sentence s​​​​​​ and an integer k​​​​​​. 
# You want to truncate s​​​​​​ such that it contains only the first k​​​​​​ words. 
# Return s​​​​​​ after truncating it.

def truncateSentence(s: str, k: int) -> str:
  # initialize empty string for truncated sentence
  res = ""
  # split sentence into a list of words
  words = s.split(" ")
  # iterate up until k (0 to k-1)
  for i in range(k):
    # add word to sentence
    res += words[i]
    # when we reach last word - we break out to avoid space
    if i == k-1:
      break
    # add spacing in between words
    res += " "
  # return truncated string
  return res

print(truncateSentence("Hello how are you Contestant", 4)) # "Hello how are you"
print(truncateSentence("What is the solution to this problem", 4)) # "What is the solution"
print(truncateSentence("chopper is not a tanuki", 5)) # "chopper is not a tanuki" 