# -*- coding: utf-8 -*-
# @Author: Yan_Daojiang
# @Date:   2019-05-17 10:39:04
# @Last Modified by:   Yan_Daojiang
# @Last Modified time: 2019-05-17 10:39:13
class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        if num==0:
            return False;
        else:
            while num!=0:
                if num%4!=0 and num!=1:
                    return False
                if num==1:
                    return True
                num=int(num/4)
        return True