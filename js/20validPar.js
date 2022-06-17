/**
 * @param {string} s
 * @return {boolean}
 */
//more js its coming along takes abit more than python
var isValid = function(s) {
    var stack = [];
    for (var i = 0; i < s.length; i++) {
        let c = s.charAt(i);

        if (c == '}' || c == ')' || c == ']') {
            let top = stack.pop();
            if (c == '}' && top == "{") {
                continue
            }
            if (c == ']' && top == "[") {
                continue
            }
            if (c == ')' && top == "(") {
                continue
            }
            return false
        } else {
            stack.push(c);
        }
    }
    if (stack.length == 0) {
        return true
    }
    return false
};