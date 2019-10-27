/*
* @Author: Yan_Daojiang
* @Date:   2019-05-13 21:54:06
* @Last Modified by:   Yan_Daojiang
* @Last Modified time: 2019-05-13 21:55:20
*/


/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    void deleteNode(ListNode* node) {
        node->val=node->next->val;
        node->next=node->next->next; 
    }
};