# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#first try after some bugs hell yes
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        def inOrder(root,new_root):
            if root !=None :
                new_root=inOrder(root.left,new_root)
                if  new_root ==None:
                    new_root=TreeNode(val=root.val)
                else:
                    cur=new_root
                    while cur.right !=None:
                        cur=cur.right
                    cur.right=TreeNode(val=root.val)
                new_root=inOrder(root.right,new_root)
            #print(new_root)
            return new_root
        
        return inOrder(root,None)
                
        
            