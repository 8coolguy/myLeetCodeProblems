/**
 * @param {number[]} prices
 * @return {number}
 */
//more js problems
var maxProfit = function(prices) {
    if (prices.length == 1) {
        return 0
    }
    var p = 0;
    var l = 0;
    var r = 1;
    while (r != prices.length) {
        if (prices[r] > prices[l]) {
            if (prices[r] - prices[l] > p) {
                p = prices[r] - prices[l];
            }
        } else {
            l = r;
        }
        r++;

    }


    return p
};