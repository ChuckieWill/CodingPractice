# -*- coding: utf-8 -*-
# @Author: Yan_Daojiang
# @Date:   2019-09-22 15:56:40
# @Last Modified by:   Yan_Daojiang
# @Last Modified time: 2019-09-22 15:56:49
class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        for i in range(0,len(A)):
            A[i] = A[i][::-1]
        for i in range(0,len(A)):
            for j in range(0,len(A[0])):
                if A[i][j] == 0:
                    A[i][j] = 1
                else:
                    A[i][j] = 0
        return A
        