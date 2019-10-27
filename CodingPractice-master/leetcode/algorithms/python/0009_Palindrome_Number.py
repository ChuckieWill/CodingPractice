# -*- coding: utf-8 -*-
# @Author: Yan_Daojiang
# @Date:   2019-08-31 08:26:57
# @Last Modified by:   Yan_Daojiang
# @Last Modified time: 2019-08-31 08:27:09
class Solution:
    def isPalindrome(self, x: int) -> bool:
        # 使用双端队列，两端弹出判断
        from collections import deque
        x=str(x)
        dq=deque(x)
        while len(dq)>1:
            if  dq.popleft() != dq.pop():
                return False
        return True