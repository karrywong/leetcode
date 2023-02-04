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
public:
    std::pair<int, int> helper(TreeNode* node, int& ans) { 
        auto leftPair = std::make_pair(node->val,node->val);
        if (node->left != nullptr) {
            leftPair = helper(node->left, ans);
            ans = min(ans, node->val - leftPair.second);
        }
            
        auto rightPair = std::make_pair(node->val,node->val);
        if (node->right != nullptr) {
            rightPair = helper(node->right, ans);
            ans = min(ans, rightPair.first - node->val);
        }
        // cout << "node.val: " << node->val << endl;
        // cout << "ans: " << ans << ", leftPair.first: " << leftPair.first << ", rightPair.second: " << rightPair.second << endl;
        return std::make_pair(leftPair.first, rightPair.second);         
    }
    
    int getMinimumDifference(TreeNode* root) {
        int ans = INT_MAX;
        helper(root, ans);
        return ans;
    }
};
