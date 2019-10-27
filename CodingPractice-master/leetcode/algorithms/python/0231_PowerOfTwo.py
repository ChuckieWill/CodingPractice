# -*- coding: utf-8 -*-
# @Author: Yan_Daojiang
# @Date:   2019-05-17 10:33:38
# @Last Modified by:   Yan_Daojiang
# @Last Modified time: 2019-05-17 10:33:46
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n==0:
            return False
        else:
            while n!=0:
                if n%2!=0 and n!=1:
                    return False
                if n==1:
                    return True
                n=int(n/2)
        return True