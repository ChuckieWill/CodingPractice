# -*- coding: utf-8 -*-
# @Author: Yan_Daojiang
# @Date:   2019-05-09 10:58:42
# @Last Modified by:   Yan_Daojiang
# @Last Modified time: 2019-05-09 10:59:25
class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        for i in range(len(A)):
            A[i]=A[i]*A[i]
        A.sort()
        return A