/*
* @Author: Yan_Daojiang
* @Date:   2019-05-17 10:30:00
* @Last Modified by:   Yan_Daojiang
* @Last Modified time: 2019-05-17 10:30:15
*/
class Solution {
public:
    bool isPowerOfTwo(int n) {
        if(n==0)
            return false;
        else{
            while(n!=0){
                if(n%2!=0&&n!=1)
                    return false;
                if(n==1)
                    break;
                 n/=2;
            }
        }
        return true;
    }
};