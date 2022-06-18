/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
//lmao this was alot eeasier than what i was trying to do before
var isAnagram = ((s, t) => s.split('').sort().join('') === t.split('').sort().join(''));