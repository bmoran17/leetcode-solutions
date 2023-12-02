# 2011. Final Value of Variable After Performing Operations - https://leetcode.com/problems/final-value-of-variable-after-performing-operations/description/
# There is a programming language with only four operations and one variable X:
#   > ++X and X++ increments the value of the variable X by 1.
#   > --X and X-- decrements the value of the variable X by 1.
# Initially, the value of X is 0.
# Given an array of strings operations containing a list of operations, return the final value of X after performing all the operations.

def finalValueAfterOperations(operations: list[str]) -> int:
  result = 0
  for i in operations:
    if i == "++X" or i =="X++":
      result += 1
    else:
      result -= 1
  return result

print(finalValueAfterOperations(["--X","X++","X++"])) # 1
print(finalValueAfterOperations(["++X","++X","X++"])) # 3
print(finalValueAfterOperations(["X++","++X","--X","X--"])) # 0