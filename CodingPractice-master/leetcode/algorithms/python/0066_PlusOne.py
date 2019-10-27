# -*- coding: utf-8 -*-
# @Author: Yan_Daojiang
# @Date:   2019-06-26 17:45:05
# @Last Modified by:   Yan_Daojiang
# @Last Modified time: 2019-06-26 17:45:11
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num=0
        for digst in digits:
            num=num*10+digst
        num=num+1
        ans=[]
        while num!=0:
            ans.append(num%10)
            num=num//10
        ans.reverse()
        return ans