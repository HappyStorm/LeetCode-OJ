/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    int maxDepth(TreeNode* root) {
        if (root == NULL) return 0;
        int depth_l=1, depth_r=1;
        depth_l = this->maxDepth(root->left);
        depth_r = this->maxDepth(root->right);
        return (depth_l>depth_r) ? depth_l+1 : depth_r+1;
    }
};