# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#missed a day but this is my solution it was a pretty simple traversal and just add the nodes from both the first tree and the second tree
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        
        #have to do it individually
        if root1==None and root2==None:
            return None
        if root1==None and root2 !=None:
            return root2
        if root1!=None and root2==None:
            return root1
        
        def traverse(root1,res):
            if root1 != None:
                res.val+=root1.val
                
            if root1.left !=None:
                if res.left ==None:
                    res.left=TreeNode()
                traverse(root1.left,res.left)
                
            if root1.right !=None:
                if res.right==None:
                    res.right=TreeNode()
                traverse(root1.right,res.right)
        merged_Tree=TreeNode()
        traverse(root1,merged_Tree)
        traverse(root2,merged_Tree)
            
        return merged_Tree
        