/*
* @Author: Yan_Daojiang
* @Date:   2019-05-14 22:58:49
* @Last Modified by:   Yan_Daojiang
* @Last Modified time: 2019-05-14 22:59:22
*/

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    int maxDepth(TreeNode* root) {
        if (root==NULL)
            return 0;
        else 
            return 1+max(maxDepth(root->left),maxDepth(root->right));
    }
public:
    int max(int num1,int num2){
        if(num1>=num2)
            return num1;
        else 
            return num2;
    }
};