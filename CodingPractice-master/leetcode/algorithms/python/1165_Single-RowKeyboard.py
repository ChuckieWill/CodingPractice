# -*- coding: utf-8 -*-
# @Author: Yan_Daojiang
# @Date:   2019-09-22 15:45:05
# @Last Modified by:   Yan_Daojiang
# @Last Modified time: 2019-09-22 15:45:13
class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        keyboard = list(keyboard)
        word = list(word)
        index =[]
        for i in range(0,len(word)):
            index.append(keyboard.index(word[i]))
        time=index[0]
        for i in range(1,len(index)):
            curtime = index[i] - index[i-1]
            if curtime>0:
                time = time + curtime
            else:
                time =time -curtime
        return time
         