/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
//js binary search
var search = function(nums, target) {
    var h =nums.length-1;
    var l =0;
    while(h>=l){
        var m= Math.floor((h+l)/2);
        if(nums[m]==target){
            return m
        }
        else if(nums[m]<target){
            l=m+1;
        }else{
            h=m-1
        }
        
    }
    return -1
};