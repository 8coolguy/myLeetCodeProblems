/**
 * @param {string} s
 * @return {boolean}
 */
//ez one for the day
var isPalindrome = function(s) {
    s = s.toLowerCase();
    var letterNumber = /^[0-9a-zA-Z]+$/;
    var l = 0;
    const isAlphaNumeric = str => /^[a-z0-9]+$/gi.test(str);
    var r = s.length - 1;
    while (r >= l) {
        console.log(s.charAt(l));
        console.log(isAlphaNumeric(s.charAt(l)));
        console.log(s.charAt(r));
        console.log(isAlphaNumeric(s.charAt(r)));


        if (isAlphaNumeric(s.charAt(l)) && isAlphaNumeric(s.charAt(r))) {
            if (s.charAt(r) == s.charAt(l)) {
                l++;
                r--;
            } else {
                return false
            }

        } else if (!isAlphaNumeric(s.charAt(l))) {
            l++;
        } else if (!isAlphaNumeric(s.charAt(r))) {
            r--;
        }

    }
    return true
};