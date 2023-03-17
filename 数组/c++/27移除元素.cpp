#include <vector>
#include <iostream>
using namespace std;

int removeElement(vector<int>& nums, int val) {

    int fast_indx = 0 ;
    int slow_indx = 0 ;
    while (fast_indx<nums.size()){
        if (nums[fast_indx] ==  val){
            fast_indx ++;

        }
        else{
            nums[slow_indx] = nums[fast_indx];
            slow_indx++;
            fast_indx++;
        }
    }
    return slow_indx;


}

int main()
{
    vector<int> a = {0,1,2,2,3,0,4,2};
    int val = 2;
    cout << removeElement(a, val) << endl;
    for(int i=0; i< a.size();i++){
        cout << a[i] << ' ';
    }
    
}
