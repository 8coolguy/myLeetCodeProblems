# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#that was no that bad
class Solution:
    #O(2log(len(list n))n)
    import heapq
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        h=[]
        for i in lists:
            cur=i
            while cur:
                heapq.heappush(h,cur.val)
                cur=cur.next
        if h:
            head=ListNode(val=heapq.heappop(h))
            cur=head
            while h:
                cur.next=ListNode(val=heapq.heappop(h))
                cur=cur.next
            return head
        return None
            
        