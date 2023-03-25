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
