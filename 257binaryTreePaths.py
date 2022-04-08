# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res=[]
        
        def findPath(root,arr,res):
            if not root.right and not root.left:
                res.append(arr+str(root.val))
            if root.right:
                findPath(root.right,arr+str(root.val)+"->",res)
            if root.left:
                findPath(root.left,arr+str(root.val)+"->",res)
                
        findPath(root,"",res)
        return res
        
