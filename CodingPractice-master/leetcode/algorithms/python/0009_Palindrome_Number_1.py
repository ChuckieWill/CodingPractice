# -*- coding: utf-8 -*-
# @Author: Yan_Daojiang
# @Date:   2019-08-31 08:33:43
# @Last Modified by:   Yan_Daojiang
# @Last Modified time: 2019-08-31 08:33:53
class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x)==str(x)[::-1]