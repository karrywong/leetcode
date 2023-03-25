/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
    // Time O(N) (average O(logN)), space O(1)
public:
    void dfs(TreeNode* node, double target) {
        if (node == nullptr) 
            return;
        if (abs(node->val - target) < abs(target-ans_)) 
            ans_ = node->val;
        if (node->val > target)
            dfs(node->left, target);
        else
            dfs(node->right, target);
    }
    int closestValue(TreeNode* root, double target) {
        ans_ = root->val;
        dfs(root, target);
        return ans_;
    }
private:
    int ans_;
};
​
