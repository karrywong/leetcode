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
    int ans=0;
    pair<int,int> dfs(TreeNode* node) {
        pair<int,int> p{0,0}, leftPair, rightPair; 
        if (node == nullptr) return p;
        
        leftPair = dfs(node->left);
        rightPair = dfs(node->right);
        
        p.first = node->val+leftPair.first+rightPair.first;
        p.second = leftPair.second+rightPair.second+1;
        int avgVal = p.first / p.second;
        
        if (node->val == avgVal) ans += 1;
        return p;
    }
    int averageOfSubtree(TreeNode* root) {
        dfs(root);
        return ans;
    }
};
