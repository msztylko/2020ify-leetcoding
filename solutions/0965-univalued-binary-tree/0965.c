/**
 *  * Definition for a binary tree node.
 *    struct TreeNode {
 *          int val;
 *          struct TreeNode *left;
 *          struct TreeNode *right;
 *    };
 */

bool isUnivalTree(struct TreeNode* root) {
        
    if (!root)
        return false;
 
        
    if(root->left && root->left->val != root->val)
        return false;
        
    else if(root->right && root->right->val != root->val)
        return false;
        
    else 
        return (
        (!root->left || isUnivalTree(root->left)) &&
        (!root->right || isUnivalTree(root->right))
        );    
}
