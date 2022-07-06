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
    vector<vector<int>> levelOrder(TreeNode* root) {
        vector<vector<int>> ans;
        queue<TreeNode*> queue;
        if(root==NULL) return ans;

        queue.push(root);
        while(!queue.empty()){
            int len = queue.size();
            vector<int> layer;
            for(int i=0; i<len; ++i){
                TreeNode *cur = queue.front();
                queue.pop();
                layer.push_back(cur->val);
                if(cur->left) queue.push(cur->left);
                if(cur->right) queue.push(cur->right);
            }
            ans.push_back(layer);
        }
        return ans;
    }
};
