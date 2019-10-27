/*
* @Author: Yan_Daojiang
* @Date:   2019-05-17 10:47:51
* @Last Modified by:   Yan_Daojiang
* @Last Modified time: 2019-05-17 10:48:05
*/
class Solution {
public:
    bool isPowerOfThree(int n) {
        if(n==0)
            return false;
        while(n!=0){
            if(n%3!=0&&n!=1)
                return false;
            if(n==1)
                return true;
            n/=3;
        }
        return true;
    }
};