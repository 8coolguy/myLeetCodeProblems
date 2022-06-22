/**
 * @param {number} n
 * @return {number}
 */
//fib
var climbStairs = function(n) {
    var dp =[];
    dp.push(0)
    dp.push(1);
    for(let i =1; i <n+1; i++){
        console.log(dp[i]+dp[i-1]);
        dp.push(dp[i]+dp[i-1]);
    }
    return dp.pop()
};