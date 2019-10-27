/*
* @Author: Yan_Daojiang
* @Date:   2019-05-17 10:41:45
* @Last Modified by:   Yan_Daojiang
* @Last Modified time: 2019-05-17 10:42:00
*/
class Solution {
public:
    bool isPowerOfFour(int num) {
        if(num==0)
            return false;
        while(num!=0){
            if(num%4!=0&&num!=1)
                return false;
            if(num==1)
                return true;
            num/=4;
        }
        return true;
    }
};