# -*- coding: utf-8 -*-
# @Author: Yan_Daojiang
# @Date:   2019-06-29 18:46:57
# @Last Modified by:   Yan_Daojiang
# @Last Modified time: 2019-06-29 18:47:04
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s=s.split()
        if len(s)==0:
            return 0
        return len(s[-1])