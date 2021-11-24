# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #since the problem wants n from the end of the list we can move node n+1 forward if first is NUll remove second
        if(n==0):
            return head
        node_b=head
        i=1
        while(i!=n+1):
            node_b=node_b.next
            i+=1
        node_a=None
        #print(node_b.val)
        while(node_b!=None):
            if(node_a==None):
                node_a=head
            else:
                node_a=node_a.next
            node_b=node_b.next
        if(node_a==None):
            head=head.next
        else:
            node_a.next=node_a.next.next
        return head
        
#works in one pass cum and is 48ms
