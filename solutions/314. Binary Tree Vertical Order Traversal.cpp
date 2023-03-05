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
    // soln by ldytmac
private: 
    // first int : col of this node, second int : row of this node
    // vector<int> : stores vals of nodes at this (row, col), use vector because may have 2 nodes of the same (row, col)
    map<int, map<int, vector<int>>> m;
    void helper(TreeNode* node, int row, int col) {
        if(!node) return;
        m[col][row].push_back(node->val);
        // this order make sure if two nodes are in the same row and column, the order should be from left to right.
        if(node->left) helper(node->left, row+1, col-1);
        if(node->right) helper(node->right, row+1, col+1);        
    }
public:
    vector<vector<int>> verticalOrder(TreeNode* root) {
        helper(root, 0, 0);
        vector<vector<int>> res;
        // add vals of each col
        for (auto colItr = m.begin(); colItr != m.end(); ++colItr) {
            vector<int> tmp;
            // add vals of each (row, col)
            for (auto rowItr = colItr->second.begin(); rowItr != colItr->second.end(); rowItr++) {
                for(int& val : rowItr->second) tmp.push_back(val);
            }
            res.push_back(tmp);
        }
        return res;
    }
};
