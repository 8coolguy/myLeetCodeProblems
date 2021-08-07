/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */


/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
//by arnav choudhury does not wok spent lots of time but only finds if it is possible to add to target sum. 
//
//

#include<assert.h>
int findLeaf(struct TreeNode* root,int sum,int targetSum);
int** pathSum(struct TreeNode* root, int targetSum, int* returnSize, int** returnColumnSizes){
    assert(root !=NULL);
    printf("Answer: %i\n",findLeaf(root,0,targetSum));
    
    return NULL;
}
int findLeaf(struct TreeNode* root,int sum,int targetSum,int* ans){
    int l=0;
    int r=0;
    sum+=root->val;
    if(root->left ==NULL && root->right==NULL){
        return sum;
    }
    if(root->left !=NULL){
        l=findLeaf(root->left,sum,targetSum);
    }
    if(root->right !=NULL){
        r=findLeaf(root->right,sum,targetSum);
    }
    
    if(l==targetSum){
        return l;
    }else if(r ==targetSum){
        return r;
    }
    return -1;
    
      
}
