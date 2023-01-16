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
    int helper(TreeNode* root, int& ans) {
        if (!root)
            return 0;
                
        int ansLeft = helper(root->left, ans);
        if (root->left)
            ansLeft = (root->val==root->left->val-1) ? ansLeft+1 : 0;
        
        int ansRight = helper(root->right, ans);
        if (root->right)  
            ansRight = (root->val==root->right->val-1) ? ansRight+1 : 0;
        
        int localMax = max(max(ansLeft, ansRight), 1);
        ans = max(ans, localMax);
        return localMax;
    }
            
    int longestConsecutive(TreeNode* root) {
        int ans = 0;
        helper(root, ans);
        return ans;
    }
};
