# -*- coding: utf-8 -*-
# @Author: Yan_Daojiang
# @Date:   2019-09-22 15:33:54
# @Last Modified by:   Yan_Daojiang
# @Last Modified time: 2019-09-22 15:34:02
class Solution:
    def fixedPoint(self, A: List[int]) -> int:
        for i in range(0,len(A)):
            if A[i] == i:
                return i
        return -1
        