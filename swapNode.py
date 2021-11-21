# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if(head ==None or head.next ==None):
            return head
        
        a=head
        b=head.next
        c=head.next.next
        head=b
        head.next=a
        head.next.next=c
        cursor =head
        while (cursor!=None and cursor.next !=None):
            if(cursor ==head):
                #head swap
                pass    
            else:
                a=cursor
                b=cursor.next
                if(b==None):
                    break
                c=cursor.next.next
                if(c==None):
                    break
                d=cursor.next.next.next
                cursor.next =c
                cursor.next.next=b
                cursor.next.next.next =d
                cursor=cursor.next
            print(cursor.val)

            cursor =cursor.next
            
        return head
            
        
        
