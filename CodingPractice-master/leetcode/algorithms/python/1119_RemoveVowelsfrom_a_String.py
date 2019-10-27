# -*- coding: utf-8 -*-
# @Author: Yan_Daojiang
# @Date:   2019-09-22 15:14:42
# @Last Modified by:   Yan_Daojiang
# @Last Modified time: 2019-09-22 15:14:51

class Solution:
    def removeVowels(self, S: str) -> str:
        vowels=['a','e','i','o','u']
        ans=""
        for i in range(0,len(S)):
            if S[i] not in vowels:
                ans=ans+S[i]
        return ans