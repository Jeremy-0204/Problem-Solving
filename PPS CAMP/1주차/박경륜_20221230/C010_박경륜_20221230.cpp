class Solution {
public:
    int missingNumber(vector<int>& nums) {
        sort(nums.begin(),nums.end());
        int n = nums.size();
        int sum = n * (n+1) / 2; // total sum of range 0 ~ n
        for(int i=0;i<nums.size();i++){
            sum=sum-nums[i]; // subtract every element in list
        }
        return sum;
    }
};