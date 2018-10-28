// Forward declaration of guess API.
// @param num, your guess
// @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
int guess(int num);

class Solution {
public:
    int guessNumber(int n) {
        if(guess(n) == 0)
            return n;
        int left = 1;
        int right = n;
        while(left < right){
            int middle = left + (right - left) / 2;
            int t = guess(middle);
            if(t == 0){
                return middle;
            }else if(t == 1){
                left = middle + 1;
            }else{
                right  = middle - 1;
            }
        }
        return left;
    }
};