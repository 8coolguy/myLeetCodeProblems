# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#really basic stuff rn just practicing trees
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        def traverse(r,arr):
            if r !=None:
                traverse(r.left,arr)
                arr.append(r.val)
                traverse(r.right,arr)
        res=[]
        traverse(root,res)
        return res
                
            
        