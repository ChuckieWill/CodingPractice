# -*- coding: utf-8 -*-
# @Author: Yan_Daojiang
# @Date:   2019-09-22 16:04:01
# @Last Modified by:   Yan_Daojiang
# @Last Modified time: 2019-09-22 16:04:08
class Solution:
    def sumOfDigits(self, A: List[int]) -> int:
        num = min(A)
        if num == 0:
            return 1
        else:
            sum=0
            while num != 0:
                sum = sum + num % 10
                num = int(num / 10)
            if sum % 2 == 1:
                return 0
            else:
                return 1