# -*- coding: utf-8 -*-
# @Author: Yan_Daojiang
# @Date:   2019-10-04 13:28:58
# @Last Modified by:   Yan_Daojiang
# @Last Modified time: 2019-10-04 13:29:09
class Solution:
    def game(self, guess: List[int], answer: List[int]) -> int:
        count = 0;
        if guess[0] == answer[0]:
            count = count + 1
        if guess[1] == answer[1]:
            count = count + 1
        if guess[2] == answer[2]:
            count = count + 1
        return count