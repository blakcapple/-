#include <vector>
#include <iostream>
using namespace std;
class Solution{
    public:
        int search(vector<int>& nums, int target){
            int left = 0;
            int right = nums.size();
            while (left<right){
                int middle = left + ((right-left)>>1);
                if (nums[middle] > target){
                    right = middle;
                }
                else if (nums[middle] < target){
                    left = middle + 1;
                }
                else{
                    return middle;
                }
            }
            return -1;
        }
};
int main()
{
    vector<int> a = {-1,0,3,5,9,10};
    int target = 9;
    Solution c1;
    int result = c1.search(a, target);
    cout << "result : " << result << endl;
}
