# -*- coding: utf-8 -*-
# @Author: Yan_Daojiang
# @Date:   2019-05-10 16:07:32
# @Last Modified by:   Yan_Daojiang
# @Last Modified time: 2019-05-10 16:18:49
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        length=(len(s))
        for i in range(int(length/2)):
            temp=s[i]
            s[i]=s[length-1-i]
            s[length-1-i]=temp
            