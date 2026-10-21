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
    bool solve(TreeNode* r, TreeNode* s){
        if(r==nullptr && s==nullptr){
            return true;
        }
        if(r==nullptr || s==nullptr)return false;

        if(r->val != s->val)return false;
        return solve(r->left,s->left) && solve(r->right,s->right);
    }

    bool isSameTree(TreeNode* p, TreeNode* q) {
       if(p==nullptr && q==nullptr){
            return true;
        } 
        if(p==nullptr || q==nullptr){
            return false;
        }
        if(p->val != q->val)return false;
        return solve(p->left,q->left) && solve(p->right,q->right);

    }
};