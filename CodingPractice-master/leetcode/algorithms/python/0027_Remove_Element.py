# -*- coding: utf-8 -*-
# @Author: Yan_Daojiang
# @Date:   2019-06-26 17:08:16
# @Last Modified by:   Yan_Daojiang
# @Last Modified time: 2019-06-26 17:08:24
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count=nums.count(val)
        for i in range(count):
            nums.remove(val)
        return len(nums)