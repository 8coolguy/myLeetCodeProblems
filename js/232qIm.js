//learned a little about class implementation in javascript
var MyQueue = function() {
    this.stack1 =[];
    this.stack2=[];
};

/** 
 * @param {number} x
 * @return {void}
 */
MyQueue.prototype.push = function(x) {
    this.stack1.push(x);
};

/**
 * @return {number}
 */
MyQueue.prototype.pop = function() {
    while(this.stack1.length !=0){
        this.stack2.push(this.stack1.pop());
    }
    let top = this.stack2.pop();
    while(this.stack2.length !=0){
        this.stack1.push(this.stack2.pop());
    }
    return top
};

/**
 * @return {number}
 */
MyQueue.prototype.peek = function() {
    while(this.stack1.length !=0){
        this.stack2.push(this.stack1.pop());
    }
    let top = this.stack2.pop();
    this.stack1.push(top);
    while(this.stack2.length !=0){
        this.stack1.push(this.stack2.pop());
    }
    return top
};

/**
 * @return {boolean}
 */
MyQueue.prototype.empty = function() {
    if(this.stack1.length != 0){
        return false
    }else{
        return true;
    }
};

/** 
 * Your MyQueue object will be instantiated and called as such:
 * var obj = new MyQueue()
 * obj.push(x)
 * var param_2 = obj.pop()
 * var param_3 = obj.peek()
 * var param_4 = obj.empty()
 */