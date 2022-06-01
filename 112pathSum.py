# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#begin the dfs train yeee
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        #dfs searcf
        def travel(root,tot,tar):
            if root:
                tot+=root.val
            else:
                return False
            if tot==tar and not root.right and not root.left:
                return True
            else:
                return travel(root.left,tot,tar) or travel(root.right,tot,tar)
        return travel(root,0,targetSum)
            
        
