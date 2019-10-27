# -*- coding: utf-8 -*-
# @Author: Yan_Daojiang
# @Date:   2019-05-12 14:51:06
# @Last Modified by:   Yan_Daojiang
# @Last Modified time: 2019-05-15 22:32:14
class Solution:
    def findComplement(self, num: int) -> int:
        #十进制数转换为二进制数
        res=""
        for i in range(2,len(bin(num))):
            if int(bin(num)[i])==0:
                res=res+"1"
            else:
                res=res+"0"   
        return int(res,2)