# -*- coding: utf-8 -*-
# @Author: Yan_Daojiang
# @Date:   2019-05-13 21:53:17
# @Last Modified by:   Yan_Daojiang
# @Last Modified time: 2019-05-13 21:54:34


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val=node.next.val
        node.next=node.next.next
