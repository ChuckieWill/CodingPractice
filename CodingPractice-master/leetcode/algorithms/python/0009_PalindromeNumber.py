# -*- coding: utf-8 -*-
# @Author: Yan_Daojiang
# @Date:   2019-06-26 17:03:31
# @Last Modified by:   Yan_Daojiang
# @Last Modified time: 2019-06-26 17:03:39
class Solution:
    def isPalindrome(self, x: int) -> bool:
        #将整数转换为字符串，再转换为列表保存在a中
        a=list(str(x))
        for i in range(int(len(a)/2)):
            if a[i]!=a[len(a)-1-i]:
                return False
        return True
        