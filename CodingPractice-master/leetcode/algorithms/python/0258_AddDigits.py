# -*- coding: utf-8 -*-
# @Author: Yan_Daojiang
# @Date:   2019-05-11 22:55:37
# @Last Modified by:   Yan_Daojiang
# @Last Modified time: 2019-05-11 22:55:55
class Solution:
    def addDigits(self, num: int) -> int:
        while num>9:
            temp=num
            buf=0
            while temp!=0:
                buf=buf+temp%10
                temp=int(temp/10)
            num=buf
        return num