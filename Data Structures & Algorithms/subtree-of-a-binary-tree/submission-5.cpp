// /**
//  * Definition for a binary tree node.
//  * struct TreeNode {
//  *     int val;
//  *     TreeNode *left;
//  *     TreeNode *right;
//  *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
//  *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
//  *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
//  * };
//  */

// class Solution {
// public:
//     bool isEqual(TreeNode* tree1, TreeNode* tree2) {
//         if (tree1 == tree2) return true;
//         if (!(tree1 && tree2)) return false;

//         return (tree1->val == tree2->val) && isEqual(tree1->left, tree2->left) &&
//                 isEqual(tree1->right, tree2->right);

// }    
//     bool isSubtree(TreeNode* root, TreeNode* subRoot) {
//         if (!subRoot) return true;
//         if (!root) return false;

//         return isEqual(root, subRoot) ||
//             isSubtree(root->left, subRoot) ||
//             isSubtree(root->right, subRoot);
//     }
// };

class Solution {
public:
    string serialize(TreeNode* node) {
        if (!node) return "#,";

        return to_string(node->val) + "," +
               serialize(node->left) +
               serialize(node->right);
    }

    bool isSubtree(TreeNode* root, TreeNode* subRoot) {
        string s1 = serialize(root);
        string s2 = serialize(subRoot);

        return s1.find(s2) != string::npos;
    }
};