/*
* @Author: Yan_Daojiang
* @Date:   2019-05-08 18:58:12
* @Last Modified by:   Yan_Daojiang
* @Last Modified time: 2019-05-08 18:58:31
*/
class Solution {
public:
    string toLowerCase(string str) {
        for(int i=0;i<str.length();i++)
            if(str[i]>=65&&str[i]<=90)
                str[i]=str[i]+32;
        return str;
    }
};