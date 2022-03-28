# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#so close to a first try but i was not thinking right and messed up and had an or instead of and whatever got it for the day
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        #the heights of the left nodes have to be plus 
        def height(root):
            if root!=None:
                return 1+max(height(root.left),height(root.right))
            else:
                return 0
            
        if root ==None:
            return True
        return (height(root.left)-height(root.right) <=1 and height(root.left)-height(root.right) >=-1) and self.isBalanced(root.right) and self.isBalanced(root.left)  
                