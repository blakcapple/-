#include <vector>
#include <iostream>
using namespace std;

int minSubArrayLen(int target, vector<int>& nums) {

    int slow_idx = 0;
    int fast_idx = 0;
    int sum = 0;
    int result = nums.size()+1;
    while (fast_idx<=nums.size()){
        if (sum < target){
            if (fast_idx >= nums.size()) break;
            sum += nums[fast_idx];
            fast_idx += 1;
        }
        else{
            int distacne = fast_idx - slow_idx;
            if (distacne < result){
                result = distacne;
            }

            sum -= nums[slow_idx];
            slow_idx += 1;
        }
    }
    if (result == nums.size()+1)return 0;
    else
        return result;

}

int main(){
    vector<int> nums = {1,1,1,1,1,1,1,1};
    int target = 11;
    cout<<minSubArrayLen(target, nums)<<endl;

}
