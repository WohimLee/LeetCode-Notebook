from __future__ import annotations

from typing import List

class Solution:
    """排序后线性合并。"""

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        # 先按左端点排序，后面的区间只可能与最后一个答案区间发生重叠。
        intervals.sort(key=lambda x: x[0])
        ans = [intervals[0][:]]
        for start, end in intervals[1:]:
            if start <= ans[-1][1]:
                ans[-1][1] = max(ans[-1][1], end)
            else:
                ans.append([start, end])
        return ans

class SolutionInPlace:
    """排序后原地写回（减少额外列表创建）。"""

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        # write 指向当前已经合并好的最后一个区间。
        intervals.sort(key=lambda x: x[0])
        write = 0
        for i in range(1, len(intervals)):
            if intervals[i][0] <= intervals[write][1]:
                intervals[write][1] = max(intervals[write][1], intervals[i][1])
            else:
                write += 1
                intervals[write] = intervals[i]
        return intervals[: write + 1]

if __name__ == "__main__":
    solution = Solution()
    intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    print(solution.merge(intervals))
