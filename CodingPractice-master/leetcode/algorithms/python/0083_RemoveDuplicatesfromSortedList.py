# -*- coding: utf-8 -*-
# @Author: Yan_Daojiang
# @Date:   2019-09-21 22:26:43
# @Last Modified by:   Yan_Daojiang
# @Last Modified time: 2019-09-21 22:27:03



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        current = head
        while current != None and current.next != None:
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next
        return head
        