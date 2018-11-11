class Solution {
public:
    int poorPigs(int buckets, int minutesToDie, int minutesToTest) {
        return ceil(log(buckets) / log(minutesToTest / minutesToDie + 1));
    }
};
int main(){
    int buckets = 1000;
    int minutesToDie = 15;
    int minutesToTest = 60;
    int count = new Solution().poorPigs(buckets, minutesToDie, minutesToTest);
    cout<<count<<endl;
    return 0;
}