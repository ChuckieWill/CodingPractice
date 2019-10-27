/*
* @Author: Yan_Daojiang
* @Date:   2019-05-09 11:22:30
* @Last Modified by:   Yan_Daojiang
* @Last Modified time: 2019-05-09 11:22:45
*/
class Solution {
public:
    int fib(int N) {
        int dp[31]={0,1,1};
        for(int i=3;i<=N;i++)
            dp[i]=dp[i-1]+dp[i-2];
        return dp[N];
    }
};