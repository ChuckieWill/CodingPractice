# -*- coding: utf-8 -*-
# @Author: Yan_Daojiang
# @Date:   2019-05-14 23:00:09
# @Last Modified by:   Yan_Daojiang
# @Last Modified time: 2019-05-14 23:00:28

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) :
        if root==None:
            return 0
        else:
            return 1+max(self.maxDepth(root.left),self.maxDepth(root.right))
    
    def max(a,b)->int:
        if a>=b:
            return a
        else: 
            return b
        