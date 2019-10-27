/*
* @Author: Yan_Daojiang
* @Date:   2019-10-04 13:28:27
* @Last Modified by:   Yan_Daojiang
* @Last Modified time: 2019-10-04 13:28:40
*/
class Solution {
public:
    int game(vector<int>& guess, vector<int>& answer) {
        int count = 0;
        if (guess[0] == answer[0])
            ++count;
        if (guess[1] == answer[1])
            ++count;
        if (guess[2] == answer[2])
            ++count;
        return count;
        
    }
};