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
        vector<vector<int>> rep;
        if (!root) return rep;
        rep.push_back({root->val});
        auto l_rep = levelOrder(root->left);         
        auto r_rep = levelOrder(root->right);
        auto l = l_rep.size(); auto r = r_rep.size();
        for (int i = 0; i < min(l, r); i++)
            l_rep[i].insert(l_rep[i].end(), r_rep[i].begin(), r_rep[i].end());
        rep.insert(rep.end(), l_rep.begin(), l_rep.end());
        if (r > l) rep.insert(rep.end(), r_rep.begin() + l, r_rep.end());
        return rep;
    }
};
