# 导入当前解法依赖的模块或类型。
from __future__ import annotations

# 导入当前解法依赖的模块或类型。
from typing import List


# 定义 Solution 类，封装该题解法。
class Solution:
    """哈希集合：只从序列起点开始向后扩展。"""

    # 定义 longestConsecutive 函数/方法。
    def longestConsecutive(self, nums: List[int]) -> int:
        # 初始化或更新变量 s。
        s = set(nums)
        # 初始化或更新变量 ans。
        ans = 0
        # 遍历当前序列，逐步推进状态。
        for x in s:
            # 判断条件是否成立，选择对应处理分支。
            if x - 1 in s:
                # 跳过本轮剩余逻辑，进入下一轮循环。
                continue
            # 初始化或更新变量 y。
            y = x
            # 当条件成立时循环处理，直到状态收敛。
            while y in s:
                # 更新变量 y，推进当前状态。
                y += 1
            # 初始化或更新变量 ans。
            ans = max(ans, y - x)
        # 返回当前函数结果。
        return ans


# 定义 SolutionBoundaryMap 类，封装该题解法。
class SolutionBoundaryMap:
    """边界长度合并：记录每段连续区间的左右边界长度。"""

    # 定义 longestConsecutive 函数/方法。
    def longestConsecutive(self, nums: List[int]) -> int:
        # 初始化或更新变量 length: dict[int, int]。
        length: dict[int, int] = {}
        # 初始化或更新变量 ans。
        ans = 0
        # 遍历当前序列，逐步推进状态。
        for x in nums:
            # 判断条件是否成立，选择对应处理分支。
            if x in length:
                # 跳过本轮剩余逻辑，进入下一轮循环。
                continue
            # 初始化或更新变量 left。
            left = length.get(x - 1, 0)
            # 初始化或更新变量 right。
            right = length.get(x + 1, 0)
            # 初始化或更新变量 cur。
            cur = left + 1 + right
            # 初始化或更新变量 length[x]。
            length[x] = cur
            # 初始化或更新变量 length[x - left]。
            length[x - left] = cur
            # 初始化或更新变量 length[x + right]。
            length[x + right] = cur
            # 初始化或更新变量 ans。
            ans = max(ans, cur)
        # 返回当前函数结果。
        return ans

