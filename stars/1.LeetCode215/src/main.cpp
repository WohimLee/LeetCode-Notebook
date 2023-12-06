
#include <iostream>
#include <vector>
#include <algorithm>
#include <random>
using namespace std;

class Solution {
public:
    int partition(std::vector<int>& nums, int left, int right) {
    int pivot = nums[right];
    int i = left;
    for (int j = left; j < right; j++) {
        if (nums[j] > pivot) {
            std::swap(nums[i], nums[j]);
            i++;
        }
    }
    std::swap(nums[i], nums[right]);
    return i;
}

int quickselect(std::vector<int>& nums, int left, int right, int k) {
    if (left == right) return nums[left];

    std::random_device rd;
    std::mt19937 gen(rd());
    std::uniform_int_distribution<> dis(left, right);
    int pivot_index = partition(nums, left, right);
    
    if (k == pivot_index) {
        return nums[k];
    } else if (k < pivot_index) {
        return quickselect(nums, left, pivot_index - 1, k);
    } else {
        return quickselect(nums, pivot_index + 1, right, k);
    }
}

int findKthLargest(std::vector<int>& nums, int k) {
    return quickselect(nums, 0, nums.size() - 1, k - 1);
}
};




int main(int argc, char** argv) {
    std::vector<int> nums = {3, 2, 1, 5, 6, 4};
    int k = 2;
    std::cout << "The " << k << "th largest element is: " << findKthLargest(nums, k) << std::endl;

    nums = {3, 2, 3, 1, 2, 4, 5, 5, 6};
    k = 4;
    std::cout << "The " << k << "th largest element is: " << findKthLargest(nums, k) << std::endl;

    return 0;
}

