/**
 * @param {number[]} nums
 * @return {number}
 */
 var maxSubArray = function(nums) {
    var dp =nums[0];
    var m=nums[0];
    for(let i =1; i < nums.length; i++){
        dp=Math.max(dp+nums[i],nums[i]);
        if(dp > m){
            m =dp;
        }
    }
    return m;
};