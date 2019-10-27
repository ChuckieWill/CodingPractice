# -*- coding: utf-8 -*-
# @Author: Yan_Daojiang
# @Date:   2019-05-09 11:37:53
# @Last Modified by:   Yan_Daojiang
# @Last Modified time: 2019-05-09 11:38:05
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res=[]
        for i in range(len(nums1)):
            if nums1[i] in nums2 and nums1[i] not in res:
                res.append(nums1[i])
        return res