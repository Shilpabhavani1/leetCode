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
    vector<int> inorderTraversal(TreeNode* root)
    {
        vector<int> res;
        stack<TreeNode*>s;
        TreeNode* node =root;
        while(true)
        {
            if(node!=NULL)
            {
                s.push(node);
            node=node->left;
            }
            else
            {
                if(s.empty()==true) break;
                node=s.top();
                s.pop();
                res.push_back(node->val);
                node=node->right;
            }
        }
        return res;
    }
    // void shilpa(TreeNode* root, vector<int>&v)
    // {
    //     if(root==NULL) return ;
    //     if(root!=NULL)
    //     {
    //         shilpa(root->left,v);
    //         v.push_back(root->val);
    //         shilpa(root->right,v);
    //     }
    // }
    // vector<int> inorderTraversal(TreeNode* root) {
    //     vector <int> v;
    //     shilpa(root,v);
    //     return v;
        
    // }
};