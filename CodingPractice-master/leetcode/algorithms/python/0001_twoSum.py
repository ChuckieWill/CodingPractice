# -*- coding: utf-8 -*-
# @Author: Yan_Daojiang
# @Date:   2019-05-01 16:05:03
# @Last Modified by: Yan_Daojiang
# @Last Modified time: 2019-05-06 22:25:50

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res=[];
        n=len(nums)
        for i in range(n):
            for j in range(i+1,n):
                if nums[i]+nums[j]==target:
                    res.append(i)
                    res.append(j)
                    return res