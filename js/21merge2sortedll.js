/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} list1
 * @param {ListNode} list2
 * @return {ListNode}
 */
//javasctip time
var mergeTwoLists = function(list1, list2) {
    if (!list1 && !list2) {
        return list1
    }
    var ll = new ListNode();
    var cur = ll;
    var cur1 = list1;
    var cur2 = list2;
    while (cur1 || cur2) {
        if (cur1 && cur2) {
            if (cur1.val <= cur2.val) {
                cur.val = cur1.val;
                cur1 = cur1.next;
            } else if (cur2) {
                cur.val = cur2.val;
                cur2 = cur2.next;
            }
        } else if (cur1) {
            cur.val = cur1.val;
            cur1 = cur1.next;
        } else {
            cur.val = cur2.val;
            cur2 = cur2.next;
        }
        if (cur1 || cur2)
            cur.next = new ListNode();
        cur = cur.next

    }
    return ll
};