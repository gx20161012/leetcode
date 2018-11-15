class Solution {
public:
    string longestPalindrome(string s) {
        if(s.empty()){
            return "";
        }
        int dp[s.size()][s.size()] = {0};
        int left = 0;
        int right = 0;
        int len = 0;
        for(int i = 0; i < s.size(); i++){
            for(int j = 0; j < i+1; j++){
                dp[j][i] = (s[i] == s[j] && (i < j+2 || dp[j+1][i-1]));
                if (dp[j][i] && len < i - j + 1) {
                    len = i - j + 1;
                    left = j;
                    right = i;
                }
            }
            dp[i][i] = 1;
        }
        return s.substr(left, right - left + 1);
    }
};