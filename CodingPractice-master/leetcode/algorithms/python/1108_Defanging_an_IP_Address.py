# -*- coding: utf-8 -*-
# @Author: Yan_Daojiang
# @Date:   2019-09-22 15:27:13
# @Last Modified by:   Yan_Daojiang
# @Last Modified time: 2019-09-22 15:27:20
class Solution:
    def defangIPaddr(self, address: str) -> str:
         return address.replace('.','[.]')      