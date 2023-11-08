# 2828. Check if a String Is an Acronym of Words - https://leetcode.com/problems/check-if-a-string-is-an-acronym-of-words/description/
def isAcronym(words: list[str], s: str) -> bool:
    acronym = ""
    for word in words:
        acronym += word[0]
    return (True if acronym == s else False)

print(isAcronym(["alice","bob","charlie"], "abc")) # True
print(isAcronym(["an","apple"], "a")) # False
print(isAcronym(["never","gonna","give","up","on","you"], "ngguoy")) # True