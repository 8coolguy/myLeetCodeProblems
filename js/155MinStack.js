
var MinStack = function() {
    this.stack =[];
};

/** 
 * @param {number} val
 * @return {void}
 */
MinStack.prototype.push = function(val) {
    this.stack.push(val);
};

/**
 * @return {void}
 */
MinStack.prototype.pop = function() {
    var tmp =this.stack.pop();

};

/**
 * @return {number}
 */
MinStack.prototype.top = function() {
    var tmp =this.stack.pop();
    this.stack.push(tmp);
    return tmp;
};

/**
 * @return {number}
 */
MinStack.prototype.getMin = function() {
    var min = this.stack[0];
    for(let i of this.stack){
        if(min > i){
            min =i;
        }
    }
    return min
};

/** 
 * Your MinStack object will be instantiated and called as such:
 * var obj = new MinStack()
 * obj.push(val)
 * obj.pop()
 * var param_3 = obj.top()
 * var param_4 = obj.getMin()
 */