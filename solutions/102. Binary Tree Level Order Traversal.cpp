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
    // Soln 0 - see similar problem 314. Binary Tree Vertical Order Traversal
    vector<vector<int>> levelOrder(TreeNode* root) {
        vector<vector<int>> ans = {};
        if (!root) return ans;
        
        std::deque<std::pair<TreeNode*, int>> deq;
        deq.push_back(std::make_pair(root, 0));
        while (!deq.empty()) {
            const auto pr = deq.front();
            const auto& node = pr.first;
            int row = pr.second;
            deq.pop_front();
​
            if (row >= ans.size()) {
                ans.push_back(vector<int> {node->val});
            } else {
                ans[row].push_back(node->val);
            }
            if (node->left) {
                deq.push_back(std::make_pair(node->left, row+1));
            } 
            if (node->right) {
                deq.push_back(std::make_pair(node->right, row+1));
            }
        }
        
        return ans;
    }
};
