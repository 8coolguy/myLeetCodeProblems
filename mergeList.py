# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if(l1==None and l2==None):
            return None
        if(l1==None or l2==None):
            if(l1==None):
                return l2
            else:
                return l1
        cur1=l1
        cur2=l2
        newList=tail_ptr=None

        while(cur1 != None and cur2 !=None):
            if(cur1.val >= cur2.val):
                if(newList==None):
                    newList=ListNode(cur2.val)
                    tail_ptr=newList
                else:
                    tail_ptr.next=ListNode(cur2.val)
                    tail_ptr=tail_ptr.next
                cur2=cur2.next
            else:
                if(newList==None):
                    newList=ListNode(cur1.val)
                    tail_ptr=newList
                else:
                    tail_ptr.next=ListNode(cur1.val)
                    tail_ptr=tail_ptr.next
                cur1=cur1.next
            #print(newList)
                
        #if one finished before the other we can jsut attach the rest
        if(cur1==None and cur2==None):
            return newList
        if(cur1==None):
            tail_ptr.next=cur2
        elif(cur2==None):
            tail_ptr.next=cur1
        return newList
            
                    
                    
                
        
