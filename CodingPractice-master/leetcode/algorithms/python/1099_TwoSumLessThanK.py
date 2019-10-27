# -*- coding: utf-8 -*-
# @Author: Yan_Daojiang
# @Date:   2019-09-22 16:55:22
# @Last Modified by:   Yan_Daojiang
# @Last Modified time: 2019-09-22 16:55:33
class Solution:
    def twoSumLessThanK(self, A: List[int], K: int) -> int:
        s=[]
        for i in range(0,len(A)):
            for j in range(i+1,len(A)):
                if A[i]+A[j]<K:
                    s.append(A[i]+A[j])
        if len(s)==0:
            return -1
        else:
            return max(s)
                    