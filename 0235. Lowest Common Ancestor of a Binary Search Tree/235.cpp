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
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        if(!root) return root;
        while(true){
            int rootVal = root->val;
            if(rootVal > p->val && rootVal > q->val)
                root = root->left;
            else if(rootVal < p->val && rootVal < q->val)
                root = root->right;
            else
                return root;
        }
    }
};
