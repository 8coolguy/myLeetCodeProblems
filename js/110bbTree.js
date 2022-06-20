/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {boolean}
 */
 var isBalanced = function(root) {
    function height(root){
            if(root){
                return 1+ Math.max(height(root.left), height(root.right))
            }
            else{
                return 0
            }
    }
    if (!root){
        return true
    }
    return (height(root.left)-height(root.right) <=1 && height(root.left)-height(root.right) >=-1) && isBalanced(root.right) && isBalanced(root.left) 
};