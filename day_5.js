/**
 * 20. Valid Parentheses https://leetcode.com/problems/valid-parentheses/description/
 * Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
 * An input string is valid if:
 * - Open brackets must be closed by the same type of brackets.
 * - Open brackets must be closed in the correct order.
 * - Every close bracket has a corresponding open bracket of the same type.
 * @param {string} s
 * @return {boolean}
 */
var isValid = function(s) {
  // create stack
  let stack = [];

  for(let i = 0; i < s.length; i++) {
      const char = s[i];
      const stackLast = stack[stack.length - 1];

      // push to stack if open char
      if (char === "{" || char === "(" || char === "[") {
          stack.push(char);
          // pop last item in stack if closing char corresponds with last item in stack 
      } else if (char === "}" && stackLast === "{" || char === "]" && stackLast === "[" || char === ")" && stackLast === "(") {
          stack.pop()
      } else {
          return false;
      }
  }
  return stack.length === 0 ? true : false;
};      

console.log(isValid("()")); // true
console.log(isValid("()[]{}")) // true
console.log(isValid("(]")); // false