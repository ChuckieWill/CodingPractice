# -*- coding: utf-8 -*-
# @Author: Yan_Daojiang
# @Date:   2019-05-17 09:57:44
# @Last Modified by:   Yan_Daojiang
# @Last Modified time: 2019-05-17 09:58:05
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        s=0
        for i in range(len(nums)+1):
            s=s+i
        return s-sum(nums)