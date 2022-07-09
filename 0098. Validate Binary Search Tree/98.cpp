/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    bool check(TreeNode* root, double minVal, double maxVal){
        if(root->val <= minVal || root->val >= maxVal) return false;
        if(root->left)
            if(!check(root->left, minVal, root->val)) return false;
        if(root->right)
            if(!check(root->right, root->val, maxVal)) return false;
        return true;
    }
    bool isValidBST(TreeNode* root) {
        if(!root || (!root->left && !root->right)) return true;
        return check(root, -DBL_MAX, DBL_MAX);
    }
};
