/**
 * Problem 1. Two Sum https://leetcode.com/problems/two-sum/description/
 * Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */

const twoSum = function(nums, target) {
  const indexes =[]
  for (let i = 0; i < nums.length; i++) {
      const num1 = nums[i];
      for (let j = 0; j < nums.length; j ++) {
          const num2 = nums[j];
          if (i !== j) {
              const add = num1 + num2
              if (add === target) {
                  indexes.push(i, j)
                  return indexes
              }
          }
      }
  }
};

console.log(twoSum([2,7,11,15], 9)); // [0, 1]
console.log(twoSum([3,2,4], 6)); // [1, 2]
console.log(twoSum([3,3], 6)); // [0, 1]
