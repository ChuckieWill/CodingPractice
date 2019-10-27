class Solution {
public:
    string removeVowels(string S) {
        for (int i = 0; i < S.length(); ++i)
            if (S[i] =='a' || S[i] == 'e' || S[i] == 'i' || S[i] == 'o' || S[i] =='u'){
                --i;    //回退一步，防止连续元音
                for (int j = i + 1; j < S.length(); ++j)
                    S[j] = S[j+1];
            }
        return S;
    }
};