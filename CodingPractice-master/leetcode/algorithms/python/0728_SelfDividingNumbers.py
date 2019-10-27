# -*- coding: utf-8 -*-
# @Author: Yan_Daojiang
# @Date:   2019-05-11 21:50:01
# @Last Modified by:   Yan_Daojiang
# @Last Modified time: 2019-05-11 21:57:58
class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        res=[]
        #外层循环控制在区间中取数
        for i in range(left,right+1):
            temp=i    #temp为当前需要进行判断的数
            #内层循环对当前的数进行判断
            while i!=0:
                m=i%10
                if m==0:    #排除包含0的情况
                    break
                elif temp%m!=0:
                    break
                i=int(i/10)
            if i==0:    #判断是否是在找到自除数时退出的循环
                res.append(temp)
        return res