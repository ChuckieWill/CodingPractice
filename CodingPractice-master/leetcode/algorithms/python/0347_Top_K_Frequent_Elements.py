# -*- coding: utf-8 -*-
# @Author: Yan_Daojiang
# @Date:   2019-06-25 17:17:13
# @Last Modified by:   Yan_Daojiang
# @Last Modified time: 2019-06-25 17:17:31
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cleannums=list(set(nums))
        numcount={}
        for num in cleannums:
            numcount[num]=nums.count(num)
        inv=[(value,key) for key,value in numcount.items() ]
        ans=[]
        for i in range(k):
            ans.append(max(inv)[1])
            inv.remove(max(inv))
        return ans