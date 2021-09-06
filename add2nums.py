#great work look to optimize`

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        #123 -> 321 
        #456 ->654
        #just adding the digits in the same positon 
        #1 5 2 7 3 9
        # just needed to add numbers back to front 
        # what if greater than 9
        #456 ->654
        #789 -> 987
        #1 11 2 13 3 15
        #try shifting left
        #1 1 2 4 3 4 6 1
        #another  example
        # 9999999->same 
        # 9999->9999
        # 18 18 18 18 9 9 9
        # 8 9 9 9 0 0 0 1
        
        def getNextNode(node):
            if node.next !=None:
                return node.next
            else:
                return ListNode()
        #assuming that the 0th ele is the first element of linked list
        firstNode =node =ListNode()
        node1 =l1
        node2 =l2
        carryOver =0
        while True:
            total =node1.val +node2.val +carryOver
            carryOver =0
            if total>9:
                total-=10
                carryOver=1
            node.val =total 
            
            if node1.next ==None and node2.next ==None:
                if carryOver >0:
                    node.next =ListNode(val =carryOver)
                    node =node.next
                break
            else:
                node.next =ListNode()
                node =node.next
                node1=getNextNode(node1)
                node2 =getNextNode(node2)
        return firstNode
            
        
        
