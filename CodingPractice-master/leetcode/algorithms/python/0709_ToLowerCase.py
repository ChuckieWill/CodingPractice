# -*- coding: utf-8 -*-
# @Author: Yan_Daojiang
# @Date:   2019-05-08 18:56:18
# @Last Modified by:   Yan_Daojiang
# @Last Modified time: 2019-05-09 11:41:44
class Solution:
    def toLowerCase(self, str: str) -> str:
        strlist=list(str)
        for i in range(len(strlist)):
            if strlist[i]>='A' and strlist[i]<='Z':
                strlist[i]=chr(ord(strlist[i])+32)
        return "".join(strlist)