# -*- coding: utf-8 -*-
# @Author: Yan_Daojiang
# @Date:   2019-06-26 18:40:43
# @Last Modified by:   Yan_Daojiang
# @Last Modified time: 2019-06-26 18:40:52
class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        ans=[]
        B=A.copy()
        for i in A:
            if i%2==0:
                ans.append(i)
                B.remove(i)
        ans+=B
        return ans