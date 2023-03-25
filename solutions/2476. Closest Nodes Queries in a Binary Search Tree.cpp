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
    // Time O(N + k*log(N)) with query.size() = k 
    vector<vector<int>> closestNodes(TreeNode* root, vector<int>& queries) {
        function<void(TreeNode*, vector<int>&)> inorder;
        inorder = [&](TreeNode* t, vector<int>& v) {
            if (t != nullptr) {
                inorder(t->left, v);
                v.push_back(t->val);
                inorder(t->right, v);
            }
        };
        vector<int> nums;
        inorder(root, nums);
        
        vector<vector<int>> ans;
        int n = nums.size();
        for (int query: queries) {
            int l = lower_bound(nums.begin(), nums.end(), query)-nums.begin();
            if (l < n && nums[l] == query)
                ans.push_back({query, query});
            else if (l == 0) 
                ans.push_back({-1, nums[0]});
            else if (l == n) 
                ans.push_back({nums[n-1], -1});
            else
                ans.push_back({nums[l-1], nums[l]});
        }
        return ans;
    }
};
//     // Time O(k* N) with query.size() = k 
//     void dfs(TreeNode* node, int query) {
//         if (node == nullptr)
//             return;
//         int nodeVal = node->val;
//         if (nodeVal == query) {
//             min_ = nodeVal;
//             max_ = nodeVal;
//             return;
//         }
//         else if (nodeVal < query) {
//             if (nodeVal > min_) min_ = nodeVal;
//             dfs(node->right, query);
//         }
//         else {
//             if (nodeVal < max_) max_ = nodeVal;
//             dfs(node->left, query);
//         }
//     }
​
//     vector<vector<int>> closestNodes(TreeNode* root, vector<int>& queries) {
//         vector<vector<int>> ans;
//         for (int query : queries) {
//             min_ = INT_MIN;
//             max_ = INT_MAX;
//             dfs(root, query);
//             int ansMin = min_ == INT_MIN ? -1 : min_;
//             int ansMax = max_ == INT_MAX ? -1 : max_;
//             ans.push_back(vector<int> {ansMin, ansMax});
//         }
//         return ans;
//     }
// private: 
//     int min_, max_;
​
