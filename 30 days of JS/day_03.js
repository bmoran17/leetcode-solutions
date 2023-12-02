/**
 * Problem 13. Roman to Integer https://leetcode.com/problems/roman-to-integer/description/
 * Given a roman numeral, convert it to an integer.
 * @param {string} s
 * @return {number}
 */
var romanToInt = function(s) {
    const symbols = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    let value = 0;

    for (let i = 0; i < s.length; i++) {
        const current = symbols[s[i]];
        const next = symbols[s[i+1]];
        if(current < next) {
            value += (next - current);
            i ++;
        } else {
            value += current
        }
    }
    return value;
};

console.log(romanToInt("III")); // 3
console.log(romanToInt("LVIII")); // 58
console.log(romanToInt("MCMXCIV")) // 1994