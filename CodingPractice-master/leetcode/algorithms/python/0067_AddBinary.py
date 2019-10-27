# -*- coding: utf-8 -*-
# @Author: Yan_Daojiang
# @Date:   2019-06-29 17:57:14
# @Last Modified by:   Yan_Daojiang
# @Last Modified time: 2019-06-29 17:57:28
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a=a[::-1]
        b=b[::-1]
        numa=0
        numb=0
        for i in range(len(a)):
            numa=numa+int(a[i])*2**i
        for j in range(len(b)):
            numb=numb+int(b[j])*2**j
        numc=bin(numa+numb)
        return numc[2:]