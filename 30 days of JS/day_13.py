# 67. Add Binary - https://leetcode.com/problems/add-binary/description/
# Given two binary strings a and b, return their sum as a binary string.

def addBinary(a: str, b: str) -> str:
  result = ""
  carry = 0
  # reverse strings
  a, b = a[::-1], b[::-1]
  #iterate until max length of string
  for i in range(max(len(a), len(b))):
    # converting string to integer representation(ASCII) 
    # subtract zero ASCII value to get actual number
    # if out of bounds - give it default value of 0
    digitA = ord(a[i]) - ord("0") if i < len(a) else 0
    digitB = ord(b[i]) - ord("0") if i < len(b) else 0

    # addition of digits and carry over
    total = digitA + digitB + carry

    # character to add into the sum string
    # remainder when divided by 2 (binary)
    # ex: 0 % 2 = 0 | 1 % 2 = 1 | 2 % 2 = 1 | 3 % 2 = 1
    char = str(total % 2)

    # add character to sum string
    result = char + result

    # update carry integer - divide by 2
    # ex: 0/2 = 0 | 1/2 = 0 | 2/2 = 1 | 3/2 = 1
    carry = total // 2

  # if carry is not zero - add a one at beginning of string
  if carry:
    result = "1" + result

  return result

print(addBinary("11", "1")) # "100"
print(addBinary("1010", "1011")) # "10101"
      