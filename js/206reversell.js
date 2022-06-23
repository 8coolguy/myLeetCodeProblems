/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
 var reverseList = function(head) {
    var cursor =null;
    var prev;
    while(head){
        prev=cursor
        cursor=head;
        head=head.next
        cursor.next=prev;
    }
    head =cursor;
    return head
    
};