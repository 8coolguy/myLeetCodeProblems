/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    var d = {};
    for (var i = 0; i < nums.length; i++) {
        var n = nums[i];

        if (d[target - n] >= 0) {
            console.log(d)
            return [d[target - n], i];
        } else {
            d[n] = i;
        }
    }

};