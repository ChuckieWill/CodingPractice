/*
* @Author: Yan_Daojiang
* @Date:   2019-05-07 21:38:48
* @Last Modified by:   Yan_Daojiang
* @Last Modified time: 2019-05-07 21:39:22
*/
class Solution {
public:
    string removeOuterParentheses(string S) {
        string res="";
        int n=0;
        for(int i=0;i<S.length();i++){
            if(S[i]=='('){
                if(n>0)
                    res+=S[i];
                n++;
            }else{
                if(n>1)
                    res+=S[i];
                n--;
            }
        }
        return res;
    }
};