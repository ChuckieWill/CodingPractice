# -*- coding: utf-8 -*-
# @Author: Yan_Daojiang
# @Date:   2019-05-17 10:19:13
# @Last Modified by:   Yan_Daojiang
# @Last Modified time: 2019-05-17 10:19:21
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(1,len(nums)):
            if(nums[i-1]==nums[i]):
                return True
        return False