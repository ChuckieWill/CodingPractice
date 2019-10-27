# -*- coding: utf-8 -*-
# @Author: Yan_Daojiang
# @Date:   2019-09-22 15:30:43
# @Last Modified by:   Yan_Daojiang
# @Last Modified time: 2019-09-22 15:30:51
class Solution:
    def anagramMappings(self, A: List[int], B: List[int]) -> List[int]:
        ans=[]
        for i in range(0,len(A)):
            ans.append(B.index(A[i]))
        return ans