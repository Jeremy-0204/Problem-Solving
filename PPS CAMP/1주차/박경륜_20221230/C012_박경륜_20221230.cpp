class Solution {
public:
    int findLucky(vector<int>& arr) {
        int cnt[501] = {}, ans = -1;
        for(int i : arr) ++cnt[i];
        for(int i : arr)
            if(cnt[i] == i && i > ans) ans = i;
        return ans;
    }
};