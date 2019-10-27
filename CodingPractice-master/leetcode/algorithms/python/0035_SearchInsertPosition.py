# -*- coding: utf-8 -*-
# @Author: Yan_Daojiang
# @Date:   2019-06-26 17:16:42
# @Last Modified by:   Yan_Daojiang
# @Last Modified time: 2019-06-26 17:16:57
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        #判断在不在
        if target in nums:
            return nums.index(target)
        else:
            nums.append(target)
            nums.sort()
            return nums.index(target)