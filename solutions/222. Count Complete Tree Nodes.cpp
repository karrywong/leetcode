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
    int computeDepth(TreeNode* node){
        int depth = 0;
        while (node->left != nullptr) {
            node = node->left;
            depth += 1;
        }
        return depth;
    }
    
    bool exists(int idx, int d, TreeNode* node) {
        int l = 0, r = pow(2,d)-1, mid;
        for (int i=0; i < d; i++) {
            mid = l + (r-l)/2;
            if (idx <= mid) {
                node = node->left;
                r = mid;}
            else {
                node = node->right;
                l = mid+1;}
        } 
        return (node != nullptr);
    }
        
    int countNodes(TreeNode* root) {
        if (root == nullptr) return 0;
        int d = computeDepth(root);
        int l = 0, r = pow(2,d)-1, pivot;
        while (l <= r) {
            pivot = l + (r-l)/2;
            if (exists(pivot, d, root)) l = pivot+1;
            else r = pivot-1;
        }
        return (pow(2,d)-1)+l;
    }
};
