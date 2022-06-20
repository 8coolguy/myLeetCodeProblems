/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
/**
 * @param {ListNode} head
 * @return {boolean}
 */
 var hasCycle = function(head) {
    var cur1 =head;
    var cur2 =head;
    while(cur1 && cur2){
        cur1=cur1.next;
        cur2=cur2.next;
        if(cur2){
            cur2=cur2.next;
        }
        if(cur1==cur2 && cur1 &&cur2){
            return true
        }
        
    }
    return false
};