/*
* @Author: Yan_Daojiang
* @Date:   2019-05-15 22:30:24
* @Last Modified by:   Yan_Daojiang
* @Last Modified time: 2019-05-15 23:29:48
*/
class Solution {
public:
    int reverse(int x) {
        int a[33];
        int num;
        double res=0;
        bool f=true;
        if(x>=2147483647||x<=-2147483648)
            return 0;
        else if(x>=0){
            f=true;
            num=x;
        }
        else{
            num=-1*x;
            f=false;
        }
        int i=1;
        while(num!=0){
            a[i]=num%10;
            i++;
            num=num/10;
        }
        for(int j=1;j<i;j++){
            res=res*10+a[j];
            if(res>=2147483647||(res*-1)<=-2147483648)
            return 0;
        }
        if(f==false)
            return -1*res;
        else
            return res;
    }
};