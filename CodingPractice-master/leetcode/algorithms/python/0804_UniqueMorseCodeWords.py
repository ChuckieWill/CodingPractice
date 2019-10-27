# -*- coding: utf-8 -*-
# @Author: Yan_Daojiang
# @Date:   2019-05-12 14:42:38
# @Last Modified by:   Yan_Daojiang
# @Last Modified time: 2019-05-12 14:42:49
class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        #利用字典建立对应关系
        litters={"a":".-","b":"-...","c":"-.-.","d":"-..","e":".","f":"..-.","g":"--.","h":"....","i":"..","j":".---","k":"-.-","l":".-..","m":"--","n":"-.","o":"---","p":".--.","q":"--.-","r":".-.","s":"...","t":"-","u":"..-","v":"...-","w":".--","x":"-..-","y":"-.--","z":"--.." }
        res=[]
        for i in range(len(words)):
            temp=words[i]
            trans=""
            for j in range(len(temp)):
               trans=trans+litters[temp[j]]
            if trans not in res:
                res.append(trans)
        return len(res)