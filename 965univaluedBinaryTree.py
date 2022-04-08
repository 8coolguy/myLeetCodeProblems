# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#easy first try submission in like 5 mins
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        def Travel(root,val):
            if (root!=None and root.val==val and Travel(root.right,val) and Travel(root.left,val)) or root==None:
                return True
            else:
                return False
        if root==None:
            return True
        else:
            return Travel(root,root.val)
                
            
                
            
