/**
 * 14. Longest Common Prefix https://leetcode.com/problems/longest-common-prefix/
 * Write a function to find the longest common prefix string amongst an array of strings.
 * If there is no common prefix, return an empty string "".
 * @param {string[]} strs
 * @return {string}
 */
var longestCommonPrefix = function(strs) {
  let prefix = "";
  if (strs.length === 0) return prefix; 
  // loop through first string's characters
  for (let i = 0; i < strs[0].length; i++) {
      const char = strs[0][i]
      for (let j = 0; j < strs.length; j++) {
          // compare character in other words
          if (strs[j][i] !== char) return prefix;
      }
      prefix = prefix + char
  }
  return prefix
};

console.log(longestCommonPrefix(["flower","flow","flight"])); // "fl"
console.log(longestCommonPrefix(["dog","racecar","car"])); // ""