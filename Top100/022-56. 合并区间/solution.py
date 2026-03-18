# 导入当前解法依赖的模块或类型。
from __future__ import annotations

# 导入当前解法依赖的模块或类型。
from typing import List


# 定义 Solution 类，封装该题解法。
class Solution:
    """排序后线性合并。"""

    # 定义 merge 函数/方法。
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # 判断条件是否成立，选择对应处理分支。
        if not intervals:
            # 返回当前函数结果。
            return []
        # 对数据排序，为后续有序处理做准备。
        intervals.sort(key=lambda x: x[0])
        # 初始化或更新变量 ans。
        ans = [intervals[0][:]]
        # 遍历当前序列，逐步推进状态。
        for start, end in intervals[1:]:
            # 判断条件是否成立，选择对应处理分支。
            if start <= ans[-1][1]:
                # 初始化或更新变量 ans[-1][1]。
                ans[-1][1] = max(ans[-1][1], end)
            # 执行上述条件均不满足时的兜底逻辑。
            else:
                # 向容器末尾追加元素，扩展结果集合。
                ans.append([start, end])
        # 返回当前函数结果。
        return ans


# 定义 SolutionInPlace 类，封装该题解法。
class SolutionInPlace:
    """排序后原地写回（减少额外列表创建）。"""

    # 定义 merge 函数/方法。
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # 判断条件是否成立，选择对应处理分支。
        if not intervals:
            # 返回当前函数结果。
            return []
        # 对数据排序，为后续有序处理做准备。
        intervals.sort(key=lambda x: x[0])
        # 初始化或更新变量 write。
        write = 0
        # 遍历当前序列，逐步推进状态。
        for i in range(1, len(intervals)):
            # 判断条件是否成立，选择对应处理分支。
            if intervals[i][0] <= intervals[write][1]:
                # 初始化或更新变量 intervals[write][1]。
                intervals[write][1] = max(intervals[write][1], intervals[i][1])
            # 执行上述条件均不满足时的兜底逻辑。
            else:
                # 更新变量 write，推进当前状态。
                write += 1
                # 初始化或更新变量 intervals[write]。
                intervals[write] = intervals[i]
        # 返回当前函数结果。
        return intervals[: write + 1]


if __name__ == "__main__":
    solution = Solution()
    intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    print(solution.merge(intervals))
