# -*- coding: utf-8 -*-
# @Author: Yan_Daojiang
# @Date:   2019-05-10 17:32:55
# @Last Modified by:   Yan_Daojiang
# @Last Modified time: 2019-05-10 17:33:25
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[int(len(nums)/2)]