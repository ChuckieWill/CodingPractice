# -*- coding: utf-8 -*-
# @Author: Yan_Daojiang
# @Date:   2019-05-09 11:21:29
# @Last Modified by:   Yan_Daojiang
# @Last Modified time: 2019-05-09 11:21:42
class Solution:
    def fib(self, N: int) -> int:
        dp=[0,1,1]
        for i in range(3,N+1):
            dp.append(dp[i-1]+dp[i-2])
        return dp[N]