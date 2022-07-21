# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        cur=head
        prev=None
        c=1
        while cur:
            if c==left:
                last=cur
                behind=None
                while c <= right:
                    print(head)
                    tmp=cur.next
                    cur.next=behind
                    behind=cur
                    cur=tmp
                    c+=1
                if prev:
                    prev.next=behind
                last.next=cur
            prev=cur    
            if cur:
                cur=cur.next
            c+=1
        if left ==1:
            return behind
        return head
            
            
        