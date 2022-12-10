#include <vector>
#include <algorithm>
#include <stdio.h>
#include <iostream>

using namespace std;

class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        if(intervals.size()<=1) return intervals;

        // 对 intervals 进行排序
        sort(intervals.begin(), intervals.end());

        vector<vector<int>> output;
        // 将第一个 interval 放入 output
        output.push_back(intervals[0]);
        for(int i=1; i<intervals.size(); i++) {
            // 如果 output 最后一个 interval 的第二项 > 遍历中的 interval 的第一项
            // 证明有交集
            if(output.back()[1] >= intervals[i][0]) 
                // 把 output 中最后一个 interval 的第二项换成两者最大的第二项
                output.back()[1] = max(output.back()[1] , intervals[i][1]);
            // 没有交集则直接放入 output
            else output.push_back(intervals[i]); 
        }
        return output;
    }
};

int main(int argc, char** argv){
    vector<vector<int>> intervals1 = {{1,3},{2,6},{8,10},{15,18}};
    vector<vector<int>> intervals2 = {{1,4},{4,5}};

    Solution s;
    vector<vector<int>> res1 = s.merge(intervals1);
    vector<vector<int>> res2 = s.merge(intervals2);

    return 0;
}