/*
* @Author: Yan_Daojiang
* @Date:   2019-05-06 21:56:45
* @Last Modified by:   Yan_Daojiang
* @Last Modified time: 2019-05-08 18:31:18
*/
class Solution {
public:
    int numJewelsInStones(string J, string S) {
        int count=0;
        for(int i=0;i<J.length();i++)
            for(int j=0;j<S.length();j++)
                if(J[i]==S[j])
                    count++;
        return count;
    }
};
