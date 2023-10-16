# 28. Find the Index of the First Occurrence in a String https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/
# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

class Solution:
  def strStr(self, haystack: str, needle: str) -> int:
    # go through every starting position that will have same length as needle
    for i in range(len(haystack) + 1 - len(needle)):
      # go through every character in needle to check match
      for j in range(len(needle)):
        # break from needle comparison if no match => next i position in haystack
        if haystack[i+j] != needle[j]:
          break
          # reach last character of needle and matches => return i position 
        if j == len(needle) - 1:
          return i
    return -1
  