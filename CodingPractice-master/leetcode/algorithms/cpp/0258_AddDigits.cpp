/*
* @Author: Yan_Daojiang
* @Date:   2019-05-11 23:01:24
* @Last Modified by:   Yan_Daojiang
* @Last Modified time: 2019-05-11 23:01:38
*/
class Solution {
public:
    int addDigits(int num) {
        int buf,temp;
        while(num>9){
            temp=num;
            buf=0;
            while(temp!=0){
                buf+=temp%10;
                temp/=10;
            }
            num=buf;
        }
        return num;
    }
};