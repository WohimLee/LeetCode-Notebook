
# Sort Colors
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.


## Example 1

- Input: nums = [2,0,2,1,1,0]
- Output: [0,0,1,1,2,2]

## Example 2

- Input: nums = [2,0,1]
- Output: [0,1,2]
 

## Constraints

- n == nums.length
- 1 <= n <= 300
- nums[i] is either 0, 1, or 2.
 

Follow up: Could you come up with a one-pass algorithm using only constant extra space?


## Solution

>Algorithm:
- Consider three pointers `low = 0, mid = 0, high = nums.size() - 1`
- The algorithm ensures that at any point, 
    - every element before low is 0
    - every element after high is 2
    - every element in between are either 0, 1 or 2 i.e. unprocessed.
- We'll use `mid` pointer to traverse and check the array elements i.e. `while(mid <= high)`. Three cases are possible:
    - `nums[mid] == 0` In this case `swap(nums[low], nums[mid])` and increment both low and mid pointer i.e. `low++ mid++`
    - `nums[mid] == 1` In this case `mid++`
    - `nums[mid] == 2` In this case `swap(nums[mid], nums[high])` and decrement high pointer i.e. `high--`

```c++
#include <vector>
#include <stdio.h>
#include <iostream>

using namespace std;

class Solution {
public:
    void sortColors(vector<int>& nums) {
        // 用三个指针 [全是0]low[未处理]mid[全是2]high
        int low = 0, mid = 0, high = nums.size() - 1;
        while(mid <= high)
        {
            // 判断 nums[mid] 是 0, 1 还是 2
            switch(nums[mid])
            {
                // 交换完再 ++
                case 0: swap(nums[low++], nums[mid++]); break;     
                case 1: mid++; break;   
                // 交换完再 --         
                case 2: swap(nums[mid], nums[high--]); break;
            }
        }
    }
};

int main(int argc, char** argv){
    vector<int> nums = {2,0,2,1,1,0};

    Solution s;
    s.sortColors(nums);
    printf("sorted nums:\n");
    for(int i: nums)
        printf("%d ", i);
    cout << endl;
    return 0;
}
```