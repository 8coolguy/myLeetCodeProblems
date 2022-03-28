# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def trv(root,arr):
            if(root!=None):
                arr.append(root.val)
                trv(root.left,arr)
                trv(root.right,arr)
        x=[]
        trv(root,x)
        return x
                
        
