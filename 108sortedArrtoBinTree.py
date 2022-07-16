# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#high speed leet code problem like 10 seconds no cap
#sunday test day
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if nums:
            mid=len(nums)//2
            root =TreeNode(nums[mid])
            root.left=self.sortedArrayToBST(nums[:mid])
            root.right=self.sortedArrayToBST(nums[mid+1:])
            return root
        return None
            
            
            