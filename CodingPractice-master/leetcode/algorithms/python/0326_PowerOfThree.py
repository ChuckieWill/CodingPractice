# -*- coding: utf-8 -*-
# @Author: Yan_Daojiang
# @Date:   2019-05-17 10:44:55
# @Last Modified by:   Yan_Daojiang
# @Last Modified time: 2019-05-17 10:46:56
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n==0:
            return False
        while n!=0:
            if n%3!=0 and n!=1:
                return False
            if n==1:
                return True;
            n=int(n/3)
        return True