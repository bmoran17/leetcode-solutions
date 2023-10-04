/**
 * Problem 9. Palindrome Number
 * Given an integer x, return true if x is a palindrome, and false otherwise.
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function(x) {
  const stringNum = x.toString();
  let reverse = "";
  for (let i = stringNum.length - 1; i >= 0; i--) {
      reverse += stringNum[i];
  }
  return stringNum === reverse;
};

console.log(isPalindrome(121)) // true
console.log(isPalindrome(-121)) // false
console.log(isPalindrome(10)) // false