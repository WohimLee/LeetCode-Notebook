#include <vector>
#include <stdio.h>
#include <iostream>

using namespace std;

class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int j=0;
        for(int i=0;i<nums.size();i++){
            if(nums[i]!=val){
                nums[j++]=nums[i];
            }
        }
        return j;        
    }
};

int main(int argc, char** argv){
    int val1 = 3, val2 = 2;
    vector<int> nums1 = {3,2,2,3};
    vector<int> nums2 = {0,1,2,2,3,0,4,2};
    vector<int>::iterator it = nums1.begin();

    Solution s;
    int res1 = s.removeElement(nums1, val1);
    int res2 = s.removeElement(nums2, val2);
    printf("res1 = %d\n", res1);
    printf("res2 = %d\n", res2);

    return 0;
}