/**
 * @param {number[]} nums
 * @return {number}
 */
 var majorityElement = function(nums) {
    const map =new Map();
    for(const i of nums){
        if(map.has(i)){
            map.set(i,map.get(i)+1)
        }else{
            map.set(i,1)
        }
    }
    let max =0;
    let max_i;
    for(const i of map.keys()){
        if(map.get(i)> max){
            max =map.get(i);
            max_i =i
        }
    }
    return max_i
};