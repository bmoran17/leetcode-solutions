# 58. Length of Last Word - https://leetcode.com/problems/length-of-last-word/description/
# Given a string s consisting of words and spaces, return the length of the last word in the string.
# A word is a maximal substring consisting of non-space characters only.

def lengthOfLastWord(s: str) -> int:
    length = 0
    for i in range(len(s) - 1, -1, -1):
        if s[i] != " ":
            length = length + 1
        if s[i] == " " and length > 0:
            return length
    return length
            
print(lengthOfLastWord("Hello World")) # 5
print(lengthOfLastWord("   fly me   to   the moon  ")) # 4
print(lengthOfLastWord("luffy is still joyboy")) # 6
print(lengthOfLastWord("a")) # 1