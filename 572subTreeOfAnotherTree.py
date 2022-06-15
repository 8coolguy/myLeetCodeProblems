# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right]
#some weird code but hey it works lol
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def dfs(r,s,t):
            
            if r and s:
                print(r.val)
                print(s.val)
                if r.val ==s.val:
                    if dfs(r.right,s.right,True) and dfs(r.left,s.left,True):
                        return True
                if not t:
                    return dfs(r.right,s,False) or dfs(r.left,s,False)
            if not r and not s:
                return True
            return False
        return dfs(root,subRoot,False)
            
        