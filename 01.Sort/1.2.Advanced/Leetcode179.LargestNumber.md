
# Largest Number
Given a list of non-negative integers `nums`, arrange them such that they form the largest number and return it.

Since the result may be very large, so you need to return a string instead of an integer.

 

## Example 1

- Input: nums = [10,2]
- Output: "210"

## Example 2

- Input: nums = [3,30,34,5,9]
- Output: "9534330"
 

## Constraints
- 1 <= nums.length <= 100
- 0 <= nums[i] <= 109


## Solution

```c++

#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
#include <stdio.h>

using namespace std;

bool compare(string a,string b){
    return a+b > b+a;
}

class Solution {
public:
    string largestNumber(vector<int>& nums) {
        // 放最后拼接的、并且已排序好的字符串
        vector<string> container;
		
        // 将数字转成字符串放入 container
        for(int i : nums){
            container.push_back(to_string(i));
            printf("push_back(%d)\n", i);
        }
        
        // 排序
        sort(container.begin(),container.end(),compare);
        // 打印排序后的结果
        printf("\nsorted container:\n");
        for(int i=0; i<container.size(); i++){
            printf("%s ", container[i].c_str());
        }printf("\n\n");
        string result;
        
        // 将排序后的 container 拼接起来
        for(int i=0; i<container.size(); i++){
            result+=container[i];
            printf("result = %s\n", result.c_str());
        }
        
        return result[0]=='0'? "0" : result;
    }
};


int main(int argc, char** argv){
    vector<int> nums = {3,30,34,5,9};
    Solution s;
    string res = s.largestNumber(nums);
    cout << res << endl;

    return 0;
}
```