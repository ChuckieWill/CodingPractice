/*
* @Author: Yan_Daojiang
* @Date:   2019-09-21 22:25:32
* @Last Modified by:   Yan_Daojiang
* @Last Modified time: 2019-09-21 22:25:51
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
    ListNode* deleteDuplicates(ListNode* head) {
        ListNode *current = head ;
        while (current && current->next)
        {
            if (current->val == current->next->val)
            {
                ListNode *del = current->next;
                current->next=current->next->next;
                delete del;
            }
            else
            {
               current=current->next;
            }
        }
        return head;
    }
};