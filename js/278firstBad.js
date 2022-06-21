/**
 * Definition for isBadVersion()
 * 
 * @param {integer} version number
 * @return {boolean} whether the version is bad
 * isBadVersion = function(version) {
 *     ...
 * };
 */

/**
 * @param {function} isBadVersion()
 * @return {function}
 */
 var solution = function(isBadVersion) {
    /**
     * @param {integer} n Total versions
     * @return {integer} The first bad version
     */
    return function(n) {
        
        var h =n;
        var l =1;
        let i=Math.floor((h+l)/2);
        while(!(!isBadVersion(i-1) && isBadVersion(i))){
            i=Math.floor((h+l)/2);
            if(isBadVersion(i)){
                h=i-1;
            }else{
                l=i+1;
            }
            
        }
        return i;
    };
};